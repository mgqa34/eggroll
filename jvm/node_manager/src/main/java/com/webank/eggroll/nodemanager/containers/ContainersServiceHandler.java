package com.webank.eggroll.nodemanager.containers;


import com.eggroll.core.config.Dict;
import com.eggroll.core.config.MetaInfo;
import com.eggroll.core.containers.container.ContainersManager;
import com.eggroll.core.containers.container.DeepSpeedContainer;
import com.eggroll.core.containers.container.WarpedDeepspeedContainerConfig;
import com.eggroll.core.containers.meta.KillContainersResponse;
import com.eggroll.core.containers.meta.StartContainersResponse;
import com.eggroll.core.containers.meta.StopContainersResponse;
import com.eggroll.core.context.Context;
import com.eggroll.core.exceptions.PathNotExistException;
import com.eggroll.core.pojo.*;
import com.google.inject.Singleton;
import com.webank.eggroll.core.meta.Containers;
import com.webank.eggroll.core.transfer.Extend;
import com.webank.eggroll.nodemanager.extend.LogStreamHolder;
import io.grpc.stub.StreamObserver;
import org.apache.commons.lang3.StringUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.stream.Collectors;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;

@Singleton
public class ContainersServiceHandler {

    Logger logger = LoggerFactory.getLogger(ContainersServiceHandler.class);

    private ExecutorService executor;

    private ContainersManager containersManager = ContainersManager.builder().build(executor);

    private StartDeepspeedContainerRequest startDeepspeedContainerRequest;


    private Path providedContainersDataDir;

    private Path containersDataDir = null;

    private synchronized Path getContainersDataDir() {
        if (containersDataDir == null) {
            String providedDataDir = providedContainersDataDir != null ? String.valueOf(providedContainersDataDir) : null;
            if (providedDataDir == null) {
                String pathStr = StaticErConf.getString(MetaInfo.CONFKEY_NODE_MANAGER_CONTAINERS_DATA_DIR, "");

                if (pathStr == null || pathStr.isEmpty()) {
                    throw new IllegalArgumentException("container data dir not set");
                }
                Path path = Paths.get(pathStr);
                if (!Files.exists(path)) {
                    try {
                        Files.createDirectory(path);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
                containersDataDir = path;
            } else {
                containersDataDir = Paths.get(providedDataDir);
            }
        }
        return containersDataDir;
    }

    public ContainersServiceHandler() {

    }

    public ContainersServiceHandler(ExecutorService executorService, Path providedContainersDataDir) {
        this.executor = executorService;
        this.providedContainersDataDir = providedContainersDataDir;
    }


    public StartContainersResponse startJobContainers(StartContainersRequest startContainersRequest) {
        if (startContainersRequest.getJobType() != null) {
            if (startContainersRequest.getJobType().equals(JobProcessorTypes.DeepSpeed.name())) {
                StartDeepspeedContainerRequest startDeepspeedContainerRequest =
                        StartDeepspeedContainerRequest.fromStartContainersRequest(startContainersRequest);
                return startDeepspeedContainers(startDeepspeedContainerRequest);
            } else {
                throw new IllegalArgumentException("unsupported job type: " + startContainersRequest.getJobType().toString());
            }
        } else {
            throw new IllegalArgumentException("job type is missing");
        }
    }

    private StartContainersResponse startDeepspeedContainers(
            StartDeepspeedContainerRequest startDeepspeedContainerRequest) {
        String sessionId = startDeepspeedContainerRequest.getSessionId();
        logger.info("(sessionId=" + sessionId + ") starting deepspeed containers");

        startDeepspeedContainerRequest.getDeepspeedConfigs().forEach((containerId, deepspeedConfig) -> {
            WarpedDeepspeedContainerConfig warpedDeepspeedContainerConfig =
                    new WarpedDeepspeedContainerConfig(deepspeedConfig);
            DeepSpeedContainer container = null;
            try {
                container = new DeepSpeedContainer(
                        sessionId,
                        containerId,
                        warpedDeepspeedContainerConfig,
                        getContainerWorkspace(sessionId, deepspeedConfig.getRank()),
                        startDeepspeedContainerRequest.getCommandArguments(),
                        startDeepspeedContainerRequest.getEnvironmentVariables(),
                        startDeepspeedContainerRequest.getFiles(),
                        startDeepspeedContainerRequest.getZippedFiles(),
                        startDeepspeedContainerRequest.getOptions()
                );
            } catch (Exception e) {
                e.printStackTrace();
            }

            containersManager.addContainer(containerId, container);
            containersManager.startContainer(containerId);
            logger.info("(sessionId=" + sessionId + ") deepspeed container started: " + containerId);
        });

        logger.info("(sessionId=" + sessionId + ") deepspeed co started");
        StartContainersResponse startContainersResponse = new StartContainersResponse();
        startContainersResponse.setSessionId(sessionId);
        return startContainersResponse;
    }


    public StopContainersResponse stopJobContainers(StopContainersRequest stopContainersRequest) {
        String sessionId = stopContainersRequest.getSessionId();
        logger.info("(sessionId=" + stopContainersRequest.getSessionId() + ")stopping containers");
        for (Long containerId : stopContainersRequest.getContainers()) {
            containersManager.stopContainer(containerId);
        }
        return new StopContainersResponse(sessionId);
    }

    public KillContainersResponse killJobContainers(KillContainersRequest killContainersRequest) {
        String sessionId = killContainersRequest.getSessionId();
        logger.info("(sessionId=" + sessionId + ") killing containers");
        for (Long containerId : killContainersRequest.getContainers()) {
            containersManager.killContainer(containerId);
        }
        KillContainersResponse killContainersResponse = new KillContainersResponse();
        killContainersResponse.setSessionId(sessionId);
        return killContainersResponse;
    }

    public DownloadContainersResponse downloadContainers(DownloadContainersRequest downloadContainersRequest) {
        String sessionId = downloadContainersRequest.getSessionId();
        Containers.ContentType contentType = downloadContainersRequest.getContentType();
        List<Integer> ranks = downloadContainersRequest.getRanks();
        String compressMethod = downloadContainersRequest.getCompressMethod();
        int level = downloadContainersRequest.getCompressLevel();
        logger.info("downloading containers, sessionId: {}, ranks: ", sessionId, ranks.stream().map(Object::toString).collect(Collectors.joining(",")));

        List<ContainerContent> contents = ranks.stream()
                .map(rank -> {
                    Path targetDir;
                    if (contentType.equals(Containers.ContentType.ALL)) {
                        targetDir = getContainerWorkspace(sessionId, rank);
                    } else if (contentType.equals(Containers.ContentType.MODELS)) {
                        targetDir = getContainerModelsDir(sessionId, rank);
                    } else if (contentType.equals(Containers.ContentType.LOGS)) {
                        targetDir = getContainerLogsDir(sessionId, rank);
                    } else {
                        throw new IllegalArgumentException("unsupported container content type: " + contentType);
                    }
                    if (compressMethod.equals(Dict.ZIP)) {
                        if (Files.exists(targetDir)) {
                            return new ContainerContent(rank, zip(targetDir, level), compressMethod);
                        } else {
                            return new ContainerContent(rank, new byte[0], compressMethod);
                        }
                    } else {
                        throw new IllegalArgumentException("compress method not supported: " + compressMethod);
                    }
                }).collect(Collectors.toList());

        return new DownloadContainersResponse(sessionId, contents);
    }

    private byte[] zip(Path path, int level) {
        logger.info("zipping path: " + path.toString());
        ByteArrayOutputStream byteStream = new ByteArrayOutputStream();
        ZipOutputStream zipOutput = new ZipOutputStream(byteStream);
        zipOutput.setLevel(level);
        try {
            Files.walk(path).forEach(subPath -> {
                if (Files.isRegularFile(subPath)) {
                    String name = path.relativize(subPath).toString();

                    try {
                        zipOutput.putNextEntry(new ZipEntry(name));
                        FileInputStream inputStream = new FileInputStream(subPath.toFile());
                        byte[] buffer = new byte[1024];
                        int bytesRead = inputStream.read(buffer);
                        while (bytesRead != -1) {
                            zipOutput.write(buffer, 0, bytesRead);
                            bytesRead = inputStream.read(buffer);
                        }
                        inputStream.close();

                        zipOutput.closeEntry();
                    } catch (Exception e) {
                        logger.error("zip file failed: {}", e.getMessage());
                    }
                }
            });
        } catch (IOException e) {
            logger.error("zip file failed: {}", e.getMessage());
        } finally {
            try {
                zipOutput.close();
            } catch (Exception e) {
                logger.error("zip file failed: {}", e.getMessage());
            }
        }
        logger.info("zipped path: " + path.toString());
        return byteStream.toByteArray();
    }

    private Path getContainerWorkspace(String sessionId, long rank) {
        return containersDataDir.resolve(sessionId).resolve(Long.toString(rank));
    }

    private Path getContainerModelsDir(String sessionId, long rank) {
        return getContainerWorkspace(sessionId, rank).resolve(Dict.MODELS);
    }

    private Path getContainerLogsDir(String sessionId, long rank) {
        return getContainerWorkspace(sessionId, rank).resolve(Dict.LOGS);
    }


    public static LogStreamHolder createLogStream(Extend.GetLogRequest request, StreamObserver<Extend.GetLogResponse> responseObserver) throws PathNotExistException {
        String sessionId = request.getSessionId();
        long line = request.getStartLine() > 0 ? request.getStartLine() : 0;
        int rank = Integer.valueOf(request.getRank());

        // 获取日志文件路径
        Path path = getContainerLogsDir(sessionId, rank);
        path = path.resolve(request.getLogType() != null ? request.getLogType() : "INFO").resolve("log");

        if (!path.toFile().exists()) {
            throw new PathNotExistException("Can not find file " + path);
        }

        String command = "tail -F -n " + line + " " + path.toString();
        return new LogStreamHolder(System.currentTimeMillis(), command, responseObserver, "running");
    }

    private static Path getContainerLogsDir(String sessionId, int rank) {
        // TODO: 根据 sessionId 和 rank 获取日志文件所在目录的逻辑
        // 返回对应的日志文件路径（Path 类型）
        return Paths.get("");
    }

}



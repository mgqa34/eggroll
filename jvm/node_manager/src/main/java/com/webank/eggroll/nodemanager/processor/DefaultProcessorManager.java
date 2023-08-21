package com.webank.eggroll.nodemanager.processor;

import com.eggroll.core.config.Dict;
import com.eggroll.core.constant.ProcessorStatus;
import com.eggroll.core.containers.meta.KillContainersResponse;
import com.eggroll.core.containers.meta.StartContainersResponse;
import com.eggroll.core.containers.meta.StopContainersResponse;
import com.eggroll.core.context.Context;
import com.eggroll.core.grpc.ClusterManagerClient;
import com.eggroll.core.pojo.*;
import com.webank.eggroll.nodemanager.containers.ContainersServiceHandler;
import com.webank.eggroll.nodemanager.service.ContainerService;
import com.webank.eggroll.nodemanager.utils.ProcessUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.BeanUtils;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;

@Service
public class DefaultProcessorManager implements ProcessorManager{


    Logger logger = LoggerFactory.getLogger(DefaultProcessorManager.class);
    private ClusterManagerClient client;

    @Resource
    private ContainerService containerService;


    private ContainersServiceHandler containersServiceHandler;

    @Override
    public ErSessionMeta startContainers(Context context, ErSessionMeta sessionMeta) {
        return containerService.operateContainers(sessionMeta, Dict.NODE_CMD_START);
    }

    @Override
    public ErSessionMeta stopContainers(Context context, ErSessionMeta sessionMeta) {
        return containerService.operateContainers(sessionMeta,Dict.NODE_CMD_STOP);
    }

    @Override
    public ErSessionMeta killContainers(Context context, ErSessionMeta sessionMeta) {
        return containerService.operateContainers(sessionMeta,Dict.NODE_CMD_KILL);
    }

    @Override
    public ErProcessor heartbeat(Context context, ErProcessor processor) {

        return client.hearbeat(processor);
    }

    @Override
    public ErProcessor checkNodeProcess(Context context, ErProcessor processor) {
        ErProcessor result = new ErProcessor();
        BeanUtils.copyProperties(processor, result);
        if (ProcessUtils.checkProcess(Integer.toString(processor.getPid()))) {
            result.setStatus(ProcessorStatus.RUNNING.name());
        } else {
            result.setStatus(ProcessorStatus.KILLED.name());
        }
        logger.info("check processor pid " + processor.getPid() + " return " + result.getStatus());
        return result;
    }

    @Override
    public StartContainersResponse startJobContainers(StartContainersRequest startContainersRequest) {
        return containersServiceHandler.startJobContainers(startContainersRequest);
    }


    @Override
    public StopContainersResponse stopJobContainers(StopContainersRequest stopContainersRequest) {
        return containersServiceHandler.stopJobContainers(stopContainersRequest);
    }

    @Override
    public KillContainersResponse killJobContainers(KillContainersRequest killContainersRequest) {
        return containersServiceHandler.killJobContainers(killContainersRequest);
    }


}

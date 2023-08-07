package com.eggroll.core.config;

import java.util.List;

public class DeepspeedContainerConfig {
    private List<Integer> cudaVisibleDevices;
    private int worldSize;
    private int crossRank;
    private int crossSize;
    private int localSize;
    private int localRank;
    private int rank;
    private String storePrefix;
    private String storeHost;
    private Integer storePort;
    private String backend;

    public List<Integer> getCudaVisibleDevices() {
        return cudaVisibleDevices;
    }

    public void setCudaVisibleDevices(List<Integer> cudaVisibleDevices) {
        this.cudaVisibleDevices = cudaVisibleDevices;
    }

    public int getWorldSize() {
        return worldSize;
    }

    public void setWorldSize(int worldSize) {
        this.worldSize = worldSize;
    }

    public int getCrossRank() {
        return crossRank;
    }

    public void setCrossRank(int crossRank) {
        this.crossRank = crossRank;
    }

    public int getCrossSize() {
        return crossSize;
    }

    public void setCrossSize(int crossSize) {
        this.crossSize = crossSize;
    }

    public int getLocalSize() {
        return localSize;
    }

    public void setLocalSize(int localSize) {
        this.localSize = localSize;
    }

    public int getLocalRank() {
        return localRank;
    }

    public void setLocalRank(int localRank) {
        this.localRank = localRank;
    }

    public int getRank() {
        return rank;
    }

    public void setRank(int rank) {
        this.rank = rank;
    }

    public String getStorePrefix() {
        return storePrefix;
    }

    public void setStorePrefix(String storePrefix) {
        this.storePrefix = storePrefix;
    }

    public String getStoreHost() {
        return storeHost;
    }

    public void setStoreHost(String storeHost) {
        this.storeHost = storeHost;
    }

    public Integer getStorePort() {
        return storePort;
    }

    public void setStorePort(Integer storePort) {
        this.storePort = storePort;
    }

    public String getBackend() {
        return backend;
    }

    public void setBackend(String backend) {
        this.backend = backend;
    }

    //    public DeepspeedContainerConfig(List<Integer> cudaVisibleDevices, int worldSize, int crossRank, int crossSize,
//                                    int localSize, int localRank, int rank, String storePrefix) {
//        this.cudaVisibleDevices = cudaVisibleDevices;
//        this.worldSize = worldSize;
//        this.crossRank = crossRank;
//        this.crossSize = crossSize;
//        this.localSize = localSize;
//        this.localRank = localRank;
//        this.rank = rank;
//        this.storePrefix = storePrefix;
//    }
//
//    public DeepspeedContainerConfig(List<Integer> cudaVisibleDevices, int worldSize, int crossRank, int crossSize,
//                                    int localSize, int localRank, int rank, String storePrefix,
//                                    String storeHost, int storePort, String backend) {
//        this(cudaVisibleDevices, worldSize, crossRank, crossSize, localSize, localRank, rank, storePrefix);
//        this.storeHost = storeHost;
//        this.storePort = storePort;
//        this.backend = backend;
//    }
//
//    public static byte[] serialize(DeepspeedContainerConfig src) {
//        Containers.DeepspeedContainerConfig.Builder builder = Containers.DeepspeedContainerConfig.newBuilder();
//        builder.addAllCudaVisibleDevices(src.getCudaVisibleDevices())
//                .setWorldSize(src.getWorldSize())
//                .setCrossRank(src.getCrossRank())
//                .setCrossSize(src.getCrossSize())
//                .setLocalSize(src.getLocalSize())
//                .setLocalRank(src.getLocalRank())
//                .setRank(src.getRank())
//                .setStoreHost(src.getStoreHost() != null ? src.getStoreHost() : "")
//                .setStorePort(src.getStorePort() != null ? src.getStorePort() : -1)
//                .setBackend(src.getBackend() != null ? src.getBackend() : "")
//                .setStorePrefix(src.getStorePrefix());
//
//        Containers.DeepspeedContainerConfig deepspeedContainerConfig = builder.build();
//        return deepspeedContainerConfig.toByteArray();
//    }
//
//    public static DeepspeedContainerConfig deserialize(ByteString byteString) {
//        try {
//            Containers.DeepspeedContainerConfig src = Containers.DeepspeedContainerConfig.parseFrom(byteString);
//            return new DeepspeedContainerConfig(
//                    src.getCudaVisibleDevicesList(),
//                    src.getWorldSize(),
//                    src.getCrossRank(),
//                    src.getCrossSize(),
//                    src.getLocalSize(),
//                    src.getLocalRank(),
//                    src.getRank(),
//                    src.getStorePrefix(),
//                    src.getStoreHost(),
//                    src.getStorePort(),
//                    src.getBackend()
//            );
//        } catch (InvalidProtocolBufferException e) {
//            e.printStackTrace();
//            return null;
//        }
//    }
}
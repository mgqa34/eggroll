package com.webank.eggroll.core.entity;

import java.util.Date;

public class ProcessorResource {
    private Long id;

    private Long processorId;

    private String sessionId;

    private Integer serverNodeId;

    private String resourceType;

    private Long allocated;

    private String extention;

    private String status;

    private Integer pid;

    private Date createdAt;

    private Date updatedAt;

    public ProcessorResource(Long id, Long processorId, String sessionId, Integer serverNodeId, String resourceType, Long allocated, String extention, String status, Integer pid, Date createdAt, Date updatedAt) {
        this.id = id;
        this.processorId = processorId;
        this.sessionId = sessionId;
        this.serverNodeId = serverNodeId;
        this.resourceType = resourceType;
        this.allocated = allocated;
        this.extention = extention;
        this.status = status;
        this.pid = pid;
        this.createdAt = createdAt;
        this.updatedAt = updatedAt;
    }

    public ProcessorResource() {
        super();
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Long getProcessorId() {
        return processorId;
    }

    public void setProcessorId(Long processorId) {
        this.processorId = processorId;
    }

    public String getSessionId() {
        return sessionId;
    }

    public void setSessionId(String sessionId) {
        this.sessionId = sessionId == null ? null : sessionId.trim();
    }

    public Integer getServerNodeId() {
        return serverNodeId;
    }

    public void setServerNodeId(Integer serverNodeId) {
        this.serverNodeId = serverNodeId;
    }

    public String getResourceType() {
        return resourceType;
    }

    public void setResourceType(String resourceType) {
        this.resourceType = resourceType == null ? null : resourceType.trim();
    }

    public Long getAllocated() {
        return allocated;
    }

    public void setAllocated(Long allocated) {
        this.allocated = allocated;
    }

    public String getExtention() {
        return extention;
    }

    public void setExtention(String extention) {
        this.extention = extention == null ? null : extention.trim();
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status == null ? null : status.trim();
    }

    public Integer getPid() {
        return pid;
    }

    public void setPid(Integer pid) {
        this.pid = pid;
    }

    public Date getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(Date createdAt) {
        this.createdAt = createdAt;
    }

    public Date getUpdatedAt() {
        return updatedAt;
    }

    public void setUpdatedAt(Date updatedAt) {
        this.updatedAt = updatedAt;
    }
}
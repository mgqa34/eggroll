package com.webank.eggroll.webapp.service;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.github.pagehelper.PageHelper;
import com.google.inject.Inject;
import com.webank.eggroll.clustermanager.dao.impl.SessionMainService;
import com.webank.eggroll.clustermanager.dao.impl.SessionProcessorService;
import com.webank.eggroll.clustermanager.entity.SessionMain;
import com.webank.eggroll.clustermanager.entity.SessionProcessor;
import com.webank.eggroll.webapp.global.ErrorCode;
import com.webank.eggroll.webapp.model.ResponseResult;
import com.webank.eggroll.webapp.queryobject.NodeDetailQO;
import com.webank.eggroll.webapp.utils.RequestUtils;

import java.util.ArrayList;
import java.util.List;

public class PrenodeSessionInfoService {

//    @Inject
//    private ServerNodeService serverNodeService;

    @Inject
    private SessionProcessorService sessionProcessorService;

    @Inject
    private SessionMainService sessionMainService;


    public Object querySession(NodeDetailQO nodeDetailQO) {
        PageHelper.startPage(nodeDetailQO.getPageNum(), nodeDetailQO.getPageSize());
        Integer nodeNum = nodeDetailQO.getNodeNum();
        String sessionId = nodeDetailQO.getSessionId();
        boolean isSessionId = (sessionId != null && !sessionId.isEmpty());
        if (nodeNum > 0) {
            return getNodeSessions(nodeNum);
        } else if (isSessionId) {
            return getNodeSessions(sessionId);
        }
        return new ResponseResult(ErrorCode.PARAM_ERROR);
    }

    public List<SessionMain> getNodeSessions(int nodeNum) {

        QueryWrapper spWrapper = new QueryWrapper();
        spWrapper.eq("server_node_id", nodeNum);
        List<SessionProcessor> sessionProcessors = sessionProcessorService.list(spWrapper);
        if (sessionProcessors == null || sessionProcessors.size() == 0) {
            return null;
        }
        List<String> sessionIds = new ArrayList<>();
        for (SessionProcessor sessionProcessor : sessionProcessors) {
            sessionIds.add(sessionProcessor.getSessionId());
        }
        if (sessionIds.size() == 0) {
            return null;
        }
        QueryWrapper sessionMainWrapper = new QueryWrapper();
        sessionMainWrapper.in("session_id", sessionIds);
        List<SessionMain> list = sessionMainService.list(sessionMainWrapper);
        return list;
    }

    public List<SessionMain> getNodeSessions(String sessionId) {
        List<String> sessionIdList = new ArrayList<>();
        sessionIdList.add(sessionId);

        List<SessionMain> list = sessionMainService.listByIds(sessionIdList);
        return list;
    }

}
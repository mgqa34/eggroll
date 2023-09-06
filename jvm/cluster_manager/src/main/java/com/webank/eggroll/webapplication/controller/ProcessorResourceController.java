package com.webank.eggroll.webapplication.controller;

import com.google.inject.Inject;
import com.google.inject.Singleton;
import com.webank.eggroll.clustermanager.entity.ProcessorResource;
import com.webank.eggroll.webapplication.dao.ProcessorResourceDao;
import com.webank.eggroll.webapplication.model.CommonResponse;
import com.webank.eggroll.webapplication.utils.JsonFormatUtil;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@Singleton
public class ProcessorResourceController extends HttpServlet {

    private ProcessorResourceDao resourceDao;

    @Inject
    public ProcessorResourceController(ProcessorResourceDao resourceDao) {
        this.resourceDao = resourceDao;
    }

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        int page = Integer.parseInt(req.getParameter("page"));
        int pageSize = Integer.parseInt(req.getParameter("pageSize"));

        CommonResponse<List<ProcessorResource>> response;
        List<ProcessorResource> resources = resourceDao.getData(page, pageSize);
        if (resources != null && !resources.isEmpty()) {
            // 获取数据成功
            response = CommonResponse.success(resources);
        } else {
            // 获取数据失败或无数据
            response = CommonResponse.error("Failed to retrieve resources.");
        }

        resp.setContentType("application/json");
        resp.setCharacterEncoding("UTF-8");

        // 将响应结果转换为 JSON 格式
        String json = JsonFormatUtil.toJson(response.getCode(),
                response.getMsg(), response.getData());

        resp.getWriter().write(json);
    }
}

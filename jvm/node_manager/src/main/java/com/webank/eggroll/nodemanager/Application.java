package com.webank.eggroll.nodemanager;

//import com.webank.eggroll.clustermanager.grpc.GrpcServer;
import com.eggroll.core.config.Dict;
import com.eggroll.core.config.ErConf;
import com.eggroll.core.config.MetaInfo;
import com.eggroll.core.utils.CommandArgsUtils;
import com.eggroll.core.utils.PropertiesUtil;
import com.webank.eggroll.nodemanager.grpc.GrpcServer;
import org.apache.commons.cli.CommandLine;
import org.slf4j.LoggerFactory;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.slf4j.Logger;
import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.ApplicationContext;


import java.io.File;
import java.io.IOException;
import java.util.Properties;

@SpringBootApplication
@ConfigurationProperties
public class Application {

    static Logger logger = LoggerFactory.getLogger(Application.class);

    public static ApplicationContext context  ;

    public static void main(String[] args) {
        System.setProperty("spring.config.name","eggroll");
        CommandLine cmd = CommandArgsUtils.parseArgs(args);
        String confPath = cmd.getOptionValue('c', "./conf/eggroll.properties");
        Properties environment = PropertiesUtil.getProperties(confPath);
        try {
            ErConf.addProperties(confPath);
            File confFile = new File(confPath);
            ErConf.getConf().put(Dict.STATIC_CONF_PATH,confFile.getAbsolutePath());
        }catch (IOException e) {
            logger.error("init erconf failed",e.getMessage());
        }

        MetaInfo.init(environment);

        context=  new SpringApplicationBuilder(Application.class).run(args);

        GrpcServer grpcServer = (GrpcServer)context.getBean("grpcServer");
        try {
            grpcServer.start();
        } catch (Exception e) {
            e.printStackTrace();
        }

        synchronized(context) {
            try {
                context.wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

    }
}

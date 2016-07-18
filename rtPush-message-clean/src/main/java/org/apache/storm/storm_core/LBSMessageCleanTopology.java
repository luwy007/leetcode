package org.apache.storm.storm_core;

import org.apache.commons.cli.CommandLine;
import org.apache.storm.storm_core.Spout.LBSMessageCleanSpout;
import org.apache.storm.storm_core.utils.PushConstants;
import org.apache.storm.storm_core.utils.PushOptionParser;
import org.apache.storm.storm_core.Bolt.*;

import backtype.storm.Config;
import backtype.storm.LocalCluster;
import backtype.storm.StormSubmitter;
import backtype.storm.topology.TopologyBuilder;
import com.dianping.commons.etl.utils.ETLUtils;

public class LBSMessageCleanTopology{
	public static void main(String[] args) throws Exception {
		//获得topology运行的相关参数
		
        PushOptionParser op = new PushOptionParser();
        CommandLine cl = op.parse(args); 
        boolean debug = Boolean.parseBoolean(cl.getOptionValue("debug"));
        int workNum = ETLUtils.parserInt(cl.getOptionValue("work_num"), 1);
        int logParserBoltNum = ETLUtils.parserInt(cl.getOptionValue("log_parser_para"), 1);
        int pushSpoutNum = ETLUtils.parserInt(cl.getOptionValue("push_spout_para"), 1); 
        
        
        Config conf = new Config();
        conf.setDebug(debug);
        conf.setNumAckers(0);
        conf.setNumWorkers(workNum);
        
        
        TopologyBuilder builder = new TopologyBuilder();
        builder.setSpout("lbs-message-clean-spout", new LBSMessageCleanSpout(), pushSpoutNum);
        builder.setBolt("log-parser-bolt", new LogParserBolt(), logParserBoltNum)
                .shuffleGrouping("lbs-message-clean-spout", "LBS_PUSH");


    
        LocalCluster cluster = new LocalCluster();
        cluster.submitTopology("LBSMessageClean", conf, builder.createTopology());
        //Thread.sleep(30000);//还是没搞懂干啥的
        //cluster.shutdown();  
        //StormSubmitter.submitTopology("RT-Push-ShopPromotion", conf, builder.createTopology());
        //System.exit(0); //exit本质是让jvm关闭
    }

}

package org.apache.storm.storm_core.Bolt;

import java.util.HashMap;
import java.util.Map;

import org.apache.commons.lang3.StringUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.dianping.cat.Cat;
import com.dianping.swallow.common.message.Destination;
import com.dianping.swallow.common.producer.exceptions.RemoteServiceInitFailedException;
import com.dianping.swallow.common.producer.exceptions.SendFailedException;
import com.dianping.swallow.producer.Producer;
import com.dianping.swallow.producer.ProducerConfig;
import com.dianping.swallow.producer.ProducerMode;
import com.dianping.swallow.producer.impl.ProducerFactoryImpl;

import backtype.storm.task.OutputCollector;
import backtype.storm.task.TopologyContext;
import backtype.storm.topology.OutputFieldsDeclarer;
import backtype.storm.topology.base.BaseRichBolt;
import backtype.storm.tuple.Fields;
import backtype.storm.tuple.Tuple;

import org.apache.storm.storm_core.utils.*;
import org.json.simple.JSONObject;
public class LogParserBolt extends BaseRichBolt{

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;  //这个是干什么用的？
	Logger LOGGER = LoggerFactory.getLogger(LogParserBolt.class); //有很多不同的Logger实现，彼此之间有什么不同
	OutputCollector collector;
	
	public void prepare(Map stormConf, TopologyContext context,
			OutputCollector collector) {
		// TODO Auto-generated method stub
		this.collector = collector;
	}

	@SuppressWarnings("unchecked")
	public void execute(Tuple input){ //每次收到tuple都会被调用
		// TODO Auto-generated method stub
		String message = input.getString(0).trim();
        if(StringUtils.isBlank(message)) {
            Cat.logEvent("lbs-message", "blank"); //logEvent(String type, String name)什么意思？type可以自定义？
            collector.ack(input);  //ack告诉spout，bolt已经处理了传过来的数据，但是不是应该放在最前面，即收到数据就回复ack
            return;
        }
        
        if (StringUtils.startsWith(message, "{\"eventList\":[")
                && StringUtils.endsWith(message, "]}")) {
            
        	Cat.logEvent("lbs-message", "valid");
            // substringBetween是从字符串的头，依次查找到尾，先找start，之后找end，都是按找到的第一个字符串为准
            message = StringUtils.substringBetween(message, "{\"eventList\":[", "]}");//这个eventlist是个什么数据类型

            
            ProducerConfig config = new ProducerConfig(); 
            // 以下设置的值与默认配置一致，可以省略
            config.setMode(ProducerMode.SYNC_MODE); 
            config.setSyncRetryTimes(0);
            config.setZipped(false);
            config.setThreadPoolSize(5);
            config.setSendMsgLeftLastSession(false);//表示异步模式时，是否重启续传
            Producer p;
            
            for (String jsonStr : LogParseUtils.getMsgList(message)) {

                Map<String, String> kvPairs = LogParseUtils.parseJsonToMap(jsonStr);
                String dpId = kvPairs.get("dpId");	//这边修改一下key值
                String lat = kvPairs.get("latitude");
                String lng = kvPairs.get("longitude");

                if (StringUtils.isBlank(dpId) || dpId.equals("0")) {
                    Cat.logEvent("singleMessage", "invalid_dpId");
                    collector.ack(input);
                    return;
                }
                if (StringUtils.isBlank(lat) || StringUtils.isBlank(lng) ||
                        (lat.equals("0.0") && lng.equals("0.0"))) {//&&不加括号不影响最终结果，但是代码阅读费劲
                    
                	Cat.logEvent("singleMessage", "invalid_lat_lng");
                    collector.ack(input);
                    return;
                }
                
                
				try { //当UserId，lat, lng都没有问题时，利用swallow的producer回传解析结果
					p = ProducerFactoryImpl.getInstance().createProducer(Destination.topic("rtPush_message"), config); //topic名称应该需要修订
                    try{
                    	JSONObject obj = new JSONObject();
                    	obj.put("dpId", dpId);
                    	obj.put("lat", lat);
                    	obj.put("lng", lng);
                    	obj.put("client", "DIANPING");
                    	obj.put("shopId", null);
                    	obj.put("action", "LOC");
                    	obj.put("actionDesc", null);
                        
                    	p.sendMessage(obj);  
                        System.out.println("Sended msg:" + obj);
                    }catch(SendFailedException e){
                        System.out.println(e);
                    }
				} catch (RemoteServiceInitFailedException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				} 
                
                Cat.logEvent("singleMessage", "valid");
            }
        }else {
            Cat.logEvent("lbs-message", "invalid");
        }

        collector.ack(input);
	}

	public void declareOutputFields(OutputFieldsDeclarer declarer) {
		// TODO Auto-generated method stub
        declarer.declareStream("log", new Fields("dpid", "latitude", "longitude"));
	}
	
	
}

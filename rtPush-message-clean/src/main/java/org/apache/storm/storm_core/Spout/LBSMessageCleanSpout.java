package org.apache.storm.storm_core.Spout;

import java.util.Map;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.TimeUnit;

import backtype.storm.spout.SpoutOutputCollector;
import backtype.storm.task.TopologyContext;
import backtype.storm.topology.IRichSpout;
import backtype.storm.topology.OutputFieldsDeclarer;
import backtype.storm.tuple.Fields;
import backtype.storm.tuple.Values;

import com.dianping.swallow.common.message.Destination;
import com.dianping.swallow.common.message.Message;
import com.dianping.swallow.consumer.BackoutMessageException;
import com.dianping.swallow.consumer.Consumer;
import com.dianping.swallow.consumer.ConsumerConfig;
import com.dianping.swallow.consumer.MessageListener;
import com.dianping.swallow.consumer.impl.ConsumerFactoryImpl;
import com.dianping.swallow.producer.impl.ProducerFactoryImpl;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


public class LBSMessageCleanSpout implements IRichSpout{
	// IRichSpout中的各个虚函数分别在什么情况下被调用
	/**
	 * IRichSpout is an interface, a lot of methods should be instantiated here
	 */
	private static final long serialVersionUID = 1L;  //do what?
	
	Logger logger = LoggerFactory.getLogger(LBSMessageCleanSpout.class);   //do what?
	SpoutOutputCollector collector;   
    ConsumerConfig config;     
    Consumer swallowConsumer;
    MyListener swallowListener;
    
	public void open(Map conf, TopologyContext context, SpoutOutputCollector collector) {
		// TODO Auto-generated method stub
		this.collector = collector;
        config = new ConsumerConfig();
        config.setThreadPoolSize(1);    
        swallowConsumer = ConsumerFactoryImpl.getInstance().createConsumer(Destination.topic("lbs_push"), "rtPush_message_clean_LBS", config);
        swallowListener = new MyListener();
        swallowConsumer.setListener(swallowListener);
        swallowConsumer.start();
	}

	public void close() {
		// TODO Auto-generated method stub
		swallowConsumer.close();
	}

	public void activate() {
		// TODO Auto-generated method stub
		swallowConsumer.start();
	}

	public void deactivate() {
		// TODO Auto-generated method stub
		swallowConsumer.close();
	}

	public void nextTuple() {
		// TODO Auto-generated method stub
		try {
            String message = swallowListener.fetchMessage();
            if (message != null) {
                collector.emit("LBS_PUSH", new Values(message));//values类是如何对传进来的复杂参数作调整的？或是不调整，直接传给之后的bolt?
            }
        } catch (InterruptedException e) {
            logger.error("fetch message wrong: " , e);
        }
	}

	public void ack(Object msgId) {
		// TODO Auto-generated method stub
		logger.debug("ack:"+msgId);
	}

	public void fail(Object msgId) {
		// TODO Auto-generated method stub
		logger.debug("fail:"+msgId);
	}

	public void declareOutputFields(OutputFieldsDeclarer declarer) {//什么作用？
		// TODO Auto-generated method stub
		declarer.declareStream("LBS_PUSH", new Fields("message"));  //streamId的作用是什么？fields作用是什么
	}

	public Map<String, Object> getComponentConfiguration() {
		// TODO Auto-generated method stub
		return null;
	}
	
	
	class MyListener implements MessageListener {
        private final Logger logger = LoggerFactory.getLogger(MyListener.class);
        private BlockingQueue<String> messageQueue;  //阻塞队列在这里的作用是什么

        public MyListener() {
            messageQueue = new LinkedBlockingQueue<String>(1000); 
            //貌似LinkedBlockingQueue可以处理并发时的问题，但spout应该是在单机上跑才对啊！为啥普通队列不行？
            try {  //这个函数是干啥的？难不成是为了减缓queue的创建速度？
                Thread.sleep(10);
            } catch (InterruptedException e) {
                logger.error("interrupted.");
            }
        }
        //Consumer接收到消息时，会调用用户实现的onMessage方法。
        public void onMessage(Message swallowMessage) throws BackoutMessageException {
        	// TODO Auto-generated method stub
            messageQueue.add(swallowMessage.getContent()); 
        }
        //Retrieves and removes the head of this queue, 
        //waiting up to the specified wait time if necessary for an element to become available.
        String fetchMessage() throws InterruptedException{  //poll本身会抛出异常，为何fetchMessage依旧要抛异常？
            return messageQueue.poll(100, TimeUnit.MILLISECONDS);
        }
    }
		
}

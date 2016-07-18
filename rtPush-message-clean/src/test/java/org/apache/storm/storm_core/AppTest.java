package org.apache.storm.storm_core;

import java.util.HashMap;
import java.util.Map;

import org.apache.commons.lang3.StringUtils;
import org.json.simple.JSONObject;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

/**
 * Unit test for simple App.
 */
public class AppTest extends TestCase
{
	public static class Message{ //将清理后的数据转化成特定格式，但现在的格式不一定正确。
		Map<String, Object> message = new HashMap<String, Object>();
		public Message(String userId, String lat, String lng, String client, String shopId, String action,String actionDesc){
			message.put("userId", userId);
			message.put("lat", lat);
			message.put("lng", lng);
			message.put("client", client);
			message.put("shopId", shopId);
			message.put("action", action);
			message.put("actionDesc", actionDesc);
		}
		public Map<String, Object> getMessage(){
			return message;
		}
	}
	public static void m1(int a, int b){
		System.out.println("double");
	}
	
	public static void m1(int a){
		System.out.println("single");
	}
    public static void main(String[] args){
    	
    	
    	m1(1,2);
    	
    	
    	System.out.println();
    	
    	
    	
    	//Message m = new Message("007", "0.0", "0.0", "DIANPING", "", "LOC", "");  	
    	//System.out.print(m.getMessage());
    	JSONObject obj = new JSONObject();
    	obj.put("userId", "123");
    	obj.put("lat", "0.0");
    	obj.put("lng", "0.0");
    	obj.put("client", "DIANPING");
    	obj.put("shopId", null);
    	obj.put("action", "LOC");
    	obj.put("actionDesc", null);
    	System.out.print(obj);
    }
}













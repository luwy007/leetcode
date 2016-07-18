package org.apache.storm.storm_core.utils;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

import org.apache.commons.lang.StringUtils;
import org.json.JSONException;
import org.json.JSONObject;

public class LogParseUtils {
	public static List<String> getMsgList(String msg) {
        List<String> msgList = new ArrayList<String>();
        int msgStart = 0;
        int msgEnd = msg.indexOf("}") + 1;
        //这边的message切分应该可以用split重构，效果可能会更好
        while(msgStart >= 0 && msgStart < msgEnd)
        {
            msgList.add(msg.substring(msgStart, msgEnd));
            msg = StringUtils.substring(msg, msgEnd + 1);

            msgStart = msg.indexOf("{");
            msgEnd = msg.indexOf("}") + 1;
        }
        return  msgList;
    }

    public static Map<String, String> parseJsonToMap(String jsonString) {
        JSONObject jsonObject = new JSONObject();

        try {
            jsonObject = new JSONObject(jsonString);
        } catch (Exception var10) {
        }

        HashMap result = new HashMap();
        Iterator iterator = jsonObject.keys();
        while(iterator.hasNext()) {
            String key = null;
            String value = null;
            key = (String)iterator.next();

            try {
                value = jsonObject.getString(key);
            } catch (JSONException var9) {
                ;
            }
            //这段代码的逻辑没看懂，什么意思？不知道。
            if(StringUtils.isBlank(value)) {//这边不是判断value是否为空吗，既然为空，为何还会有下述操作？
                if(!"latitude".equals(key) && !"longitude".equals(key)) {
                    try {
                        value = Long.toString(jsonObject.getLong(key));
                    } catch (Exception var7) {
                        ;
                    }
                }
                else if("onConnect".equals(key) || "valid" .equals(key)) {
                    try {
                        value = Boolean.toString(jsonObject.getBoolean(key));
                    } catch (Exception var) {

                    }
                }
                else {
                    try {
                        value = Double.toString(jsonObject.getDouble(key));
                    } catch (Exception var8) {
                        ;
                    }
                }
            }

            if(StringUtils.isNotBlank(value)) {
                result.put(key, value.toLowerCase());
            }
        }

        return result;
    }
   

}

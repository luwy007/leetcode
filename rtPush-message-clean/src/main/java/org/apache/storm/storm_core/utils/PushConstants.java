package org.apache.storm.storm_core.utils;

import java.util.Arrays;
import java.util.List;

public class PushConstants {
    //name of options
    public static final String TOPOLOGY_NAME = "RT-Push-ShopPromotion";
    public static final String OPTION_DEBUG_ENABLE = "debug";
    public static final String OPTION_WORK_NUM = "work_num";
    public static final String OPTION_PUSH_SPOUT_PARALLELISM_NUM = "push_spout_para";
    public static final String OPTION_LOG_PARSER_PARALLELISM_NUM = "log_parser_para";
    public static final String OPTION_PUSH_PREPROCESS_PARALLELISM_NUM = "push_pre_para";
    public static final String OPTION_PUSH_RULE_PARALLELISM_NUM = "push_rule_para";

    public static final String redisTable = "bi.dp_userid_accesstime.dim";
    public static final String redisKeyPrefix = "push-pro-";

    public static final String STREAM_NAME_LSB_PUSH = "lsb_push";
    public static final String STREAM_NAME_LOG_PARSER = "log";
    public static final String STREAM_NAME_PREPROCESS = "rule";

    //schema fields
    public static final String SCHEMA_CLIENT_TYPE = "clientType";
    public static final String SCHEMA_DPID = "dpId";
    public static final String SCHEMA_IP = "ip";
    public static final String SCHEMA_NETWORK = "network";
    public static final String SCHEMA_LATITUDE = "latitude";
    public static final String SCHEMA_LONGITUDE = "longitude";
    public static final String SCHEMA_COORD_TYPE = "coordType";
    public static final String SCHEMA_EVENT_ID = "eventId";
    public static final String SCHEMA_SOURCE = "source";
    public static final String SCHEMA_GENERATE_TIME = "generateTime";
    public static final String SCHEMA_CONNECTED_WIFI_MAC = "connectedWifiMac";
    public static final String SCHEMA_ON_CONNECT = "onConnect";
    public static final String SCHEMA_VALID = "valid";

    //这句话暂时被注释掉，貌似这个变量是用来确定位置的
    //public static final Location POI_DP_LOCATION = new Location(121.41625555420325,31.216644337438282);
    public static final double PUSH_DISTANCE_THRESHOLD = 100.0;
    public static final double PUSH_POI_AMOUNT = 10;
    public static final int PUSH_RULE_VISIT_DAY = 7;

    //tick tuple emit frequency
    public static final int PUSH_SHOP_UPDATE_FREQUENCY_IN_SECONDS = 300;    //5min update push shop list
    public static final int UPDATE_PUSH_SHOP_REMAIN_FREQUENCY_INSECONDS = 30;      //30s update push shop remain amout
    //spout\bolt names

//    public static final String[] DPID_STR_LIST = {"1002649833042063551", "-1981700438207967864", "8938031843403114304", "8253713127563459327","5857189566569891637"};

    public static final String[] DPID_STR_LIST = {"1002649833042063551","4773270092468573714","-2201698298920098343","-1461108177081287816","-7310785336642653407","-3920925858119303365","5857189566569891637","-1981700438207967864","6499612310855466703","2657161093256024658"};
    public static final List<String> DPID_LIST = Arrays.asList(DPID_STR_LIST);

}
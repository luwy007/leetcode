package org.apache.storm.storm_core.utils;

import org.apache.commons.cli.Options;

import com.dianping.commons.etl.utils.OptionParser;
import org.apache.storm.storm_core.utils.PushConstants;;

public class PushOptionParser extends OptionParser{ 
	@Override
    protected Options buildOptions() {
        Options options = new Options();
        options.addOption(PushConstants.OPTION_DEBUG_ENABLE, Boolean.TRUE, "OPTION_DEBUG_ENABLE");
        options.addOption(PushConstants.OPTION_WORK_NUM, Boolean.TRUE, "OPTION_WORK_NUM");
        options.addOption(PushConstants.OPTION_PUSH_SPOUT_PARALLELISM_NUM, Boolean.TRUE, "OPTION_SPOUT_PARALLEMISM_NUM");
        options.addOption(PushConstants.OPTION_LOG_PARSER_PARALLELISM_NUM, Boolean.TRUE, "OPTION_LOG_PARSER_PARALLELISM_NUM");
        options.addOption(PushConstants.OPTION_PUSH_PREPROCESS_PARALLELISM_NUM, Boolean.TRUE, "OPTION_PUSH_PREPROCESS_PARALLELISM_NUM");
        options.addOption(PushConstants.OPTION_PUSH_RULE_PARALLELISM_NUM, Boolean.TRUE, "OPTION_PUSH_RULE_PARALLELISM_NUM");
        return options;
    }
}

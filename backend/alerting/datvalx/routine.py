# -*- coding: utf-8 -*-


from alerting.datvalx.core.last_data import last_data
from alerting.datvalx.core.battery_level import battery_level
from alerting.datvalx.core.prs_qos import prs_qos
from alerting.datvalx.core.rain_sum import rain_sum


CHECK_FACTORY = {
    "last_data": last_data,
    "battery_level": battery_level,
    "prs_qos": prs_qos,
    "rain_sum": rain_sum,
}


def run(id, source_name, variable_name, check_name, param_set, blacklist):

    func = CHECK_FACTORY.get(check_name)
    
    func(id, source_name, variable_name, param_set, blacklist)

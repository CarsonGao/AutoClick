# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Params
from util.log import Logger

def open_model_config(deviceModel):

    dict_deviceModel={
        "default" : "default",
        "OPPO_R9_Plusm_A": "OPPO",

        "vivo_Y67A" : "vivo",

        "MI_5": "Xiaomi",
        "Redmi_Note_4": "Xiaomi",
        "2014501": "Xiaomi",
        "Redmi_Note_3": "Xiaomi",
        "MI_2" : "Xiaomi", #安装后无法打开

        "SM-G9300": "samsung",

        "1503-A01": "360",

        "Lenovo_K30-TM": "Lenovo",
        "Lenovo_A828t": "Lenovo",

        "F103": "gionee",

        "HLJ6": "xlj",
        "LA-S6": "xlj",

        "D9": "yunso",

        "OYSIN_X8": "oysin"

    }
    try:
        if deviceModel in dict_deviceModel:
            return dict_deviceModel[deviceModel]
        else:
            return dict_deviceModel['default']
    except:
        log = Logger()
        log.error("model_config.py, open_model_config : get model error")
        return dict_deviceModel['default']
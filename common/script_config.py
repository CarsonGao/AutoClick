# -*- coding: utf-8 -*-
from util.log import Logger

def open_script_config(productModel):

    dict_script = {
    "default" : "default",#没有适配的手机

	"Xiaomi": "default",
	"samsung" : "default",
	"360" : "default",
	"Lenovo" : "default",
	"vivo" : "default",

    "HUAWEI" : "default",

	"OPPO": "default",

	"gionee" : "default",
	"xlj" : "default",
	"yunso" : "default",
	"oysin" : "default"

    }

    try:
        if productModel in dict_script:
            return dict_script[productModel]
        else:
            return dict_script['default']
    except:
        log = Logger()
        log.error("model_config.py, open_model_config : get model error")
        return dict_script['default']
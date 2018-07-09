# -*- coding: utf-8 -*-
"""
调取配置文件和屏幕分辨率的代码
"""
import os
import sys
import json

def open_model_config():
    """
    获取机型对应品牌信息 oppo
    """
    config_file = r"{path}/config/model.json".format(path=sys.path[0])
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            return json.load(f)

def open_script_config():
    """
    获取品牌使用的运行包 default
    """
    config_file = r"{path}/config/script.json".format(path=sys.path[0])
    if os.path.exists(config_file):
        with open(config_file, 'r' ) as f:
            return json.load(f)


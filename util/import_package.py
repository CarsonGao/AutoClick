# -*- coding: utf-8 -*-

import importlib
#根据手机品牌不同，动态导入py脚本包
def dynamic_import(deviceModel):
    return importlib.import_module(deviceModel)
# -*- coding: utf-8 -*-

import sys

from util.import_package import dynamic_import

from common.model_config import open_model_config
from common.script_config import open_script_config
from util.device_handle import DeviceHandle
from util.android_info import android_info
from util.log import Logger

device = DeviceHandle()

#检查手机连接是否成功
is_connect = device.test_device_connect()

debug = False  #dubug模式

#手机连接成功
if is_connect:
    #运行debug
    if debug:
       info = android_info() #则将手机信息保存到android_info.txt中
       info.run()
       log = Logger()
       log.info("debug is open")

    #获取手机型号信息 OPPO_R9_Plusm_A
    deviceModel = device.getModel()

    #获取机型对应的品牌 oppo、xiaomi
    productModel = open_model_config(deviceModel)
    if productModel=='':
        productModel = device.getBrand()#如果未从列表中获取对应的品牌，则获取手机中的品牌信息做匹配


    #根据获得的品牌获得对应的运行模块
    json_script = open_script_config(productModel)

    #动态导入要运行的包\lib\xxx
    package_name = 'script.' + json_script
    runner = dynamic_import(package_name)
    runner.run.auto_run(productModel, deviceModel)

else:
    sys.exit(1)

    

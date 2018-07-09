# -*- coding: utf-8 -*-
import re

from common.model_text_config import get_model_text
from util.install_app_by_ET import Event
from util.install_app_by_sax import Element
from util.device_handle import DeviceHandle
from util.log import Logger

class run():
    @classmethod
    def auto_run(self, productModel, deviceModel):

        event = Event()
        dev = DeviceHandle()
        #获取机型text
        model_text = get_model_text(productModel)

        while True:
            # 获取手机助手进程是否运行
            app_up = dev.getProcess()  # 进程是否运行
            if app_up:# 如果进程运行则跳过
                break
            else:  # 否则看是否已经安装
                is_install = dev.get_apk_install()
                if is_install:  # 如果已经安装则运行它
                    dev.activity_app()
                else:
                    log = Logger()
                    log.error("default.py, auto_run : app install but can not run")
                    exit(1)


        while True:
            #获取当前想xml中text值
            Element.get_uidump()
            allText = Element.findElementAllText()
            #allText = Element.findElementAllText()

            for text in allText:
                over_key = re.match(u'手机取证助手', text)
                if over_key:
                    log = Logger()
                    log.info("{} install app  over".format(deviceModel))
                    exit(0)
                else:
                    if text in model_text:
                        coordinate = allText[text]
                        try:
                            event.touch(coordinate[0], coordinate[1])
                        except:
                            log = Logger()
                            log.info("default.py, auto_run : The coordinates are not available ")
                            break

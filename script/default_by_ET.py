# -*- coding: utf-8 -*-
import re


from common.model_text_config import get_model_text
from util.install_app_by_ET import Event
from util.install_app_by_ET import Element
from util.device_handle import DeviceHandle
#from util.sax_xml import Element


class run():
    @classmethod
    def auto_run(self, productModel):

        event = Event()
        element = Element()
        dev = DeviceHandle()
        #获取机型text
        model_text = get_model_text(productModel)
        while True:
            #获取手机助手进程是否运行
            app_up =dev.getProcess()#进程是否运行
            if app_up:#如果安装则跳过
                pass
            else:#否则看是否已经安装
                is_install = dev.get_apk_install()
                if is_install:#如果已经安装则运行它
                    dev.activity_app()
                else:
                    pass
            #获取当前想xml中text值
            allText = element.findElementAllText()
            #allText = Element.findElementAllText()

            for text in allText:
                #print(text)
                over_key = re.match(u'手机取证助手', text)
                if over_key:
                    exit(0)
                else:
                    if text in model_text:
                        coordinate = allText[text]
                        try:
                            event.touch(coordinate[0], coordinate[1])
                        except:
                            break

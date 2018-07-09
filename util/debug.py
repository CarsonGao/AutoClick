# -*- coding: utf-8 -*-
"""
这是debug的代码，当DEBUG_SWITCH开关开启的时候，会将各种信息存在本地，方便检查故障
"""
import os
import time
from util.device_handle import DeviceHandle

class debug():

    def __init__(self):
        device = DeviceHandle()
        self.deviceModel = device.getModel()
        self.deviceModel.split()
        self.deviceModel = '_'.join(self.deviceModel.split())

    #获取当前页码的xml
    def debug_uidump(self):

        times = self.curr_time()
        temp_parent_path = os.path.dirname(os.getcwd())
        xml_path_parent = temp_parent_path + '\\debug'+ '\\' + self.deviceModel
        if (os.path.exists(xml_path_parent) == False):
            os.makedirs(xml_path_parent)
        xml_path = xml_path_parent + '\\{}.xml'.format(times)
        run_command = "adb pull /data/local/tmp/uidump.xml {path}".format(path=xml_path)
        os.popen("adb shell uiautomator dump /data/local/tmp/uidump.xml")
        print run_command
        os.popen(run_command)

    #截屏
    def get_screen(self):
        times = self.curr_time()
        temp_parent_path = os.path.dirname(os.getcwd())
        xml_path_parent = temp_parent_path + '\\debug'+ '\\' + self.deviceModel + '\\{}.png'.format(times)
        run_command = "adb pull /data/local/tmp/temp.png  {path}".format(path=xml_path_parent)
        os.popen("adb shell screencap -p /data/local/tmp/temp.png")
        print run_command
        os.popen(run_command)

    def curr_time(self):

        times = time.strftime("%H%M%S")
        return  times

    def run_debug(self):
        while True:
            self.debug_uidump()
            self.get_screen()
            time.sleep(3)

if __name__ == '__main__':
    run = debug()
    run.run_debug()
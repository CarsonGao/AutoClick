# -*- coding: utf-8 -*-
import os

class android_info():

    def __init__(self):
        self.commands = [
            #'adb shell getprop' 查所有的信息
            #手机型号
            'adb -d shell getprop ro.product.model',
            'adb shell getprop ro.build.version.release',
            'adb shell settings get secure android_id',
            'adb get-serialno',
            'adb shell wm density',
            'adb shell wm size',
            'adb shell getprop ro.product.brand',
            'adb shell getprop ro.build.version.sdk',
            'adb shell cat /sys/class/net/wlan0/address'
        ]

    def run(self):
        outputs = ''
        i = 0
        for command in self.commands:
            process = os.popen(command)
            output = process.read()
            output = output.replace("\r\n", '')
            if i< 8:

                outputs += output + ',  '
                i += 1
            else:
                outputs += output + '\r\n'


        temp_parent_path = os.getcwd()
        with open(temp_parent_path + '\\config\\android_info.txt', "a") as f:
            f.write(outputs)


if __name__ == '__main__':
    s = android_info()
    s.run()


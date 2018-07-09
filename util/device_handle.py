# -*- coding: utf-8 -*-

import subprocess
from util.log import Logger

class DeviceHandle:
    def __init__(self):

        self.log = Logger()
    # 检测手机是否连接成功
    def getID(self):

        adbOutInfo = []
        outInfo = subprocess.Popen('adb devices', shell=True, stdout=subprocess.PIPE)
        out, err = outInfo.communicate()

        for line in out.splitlines():
            adbOutInfo.append(line)
        ID = adbOutInfo[1].split('\t')[0]

        return ID

    # 获取手机型号
    def getModel(self):
        try:
            adbOutModel = []
            outInfo = subprocess.Popen('adb -d shell getprop ro.product.model', shell=True, stdout=subprocess.PIPE)
            out, err = outInfo.communicate()

            for line in out.splitlines():
                adbOutModel.append(line)
            model = adbOutModel[0]
            model = '_'.join(model.split())  # 将空格全部变成下划线_
            return model
        except:
            self.log.error("device_handle.py, getModel : devices disconnect")
            exit(1)

    #获取api_level
    def getAPILeve(self):
        outInfo = subprocess.Popen('adb shell getprop ro.build.version.sdk', shell=True, stdout=subprocess.PIPE)
        apiLevel, err = outInfo.communicate()
        return int(apiLevel)

    #获取手机商标 oppo vivo
    def getBrand(self):
        try:
            outInfo = subprocess.Popen('adb shell getprop ro.product.brand', shell=True, stdout=subprocess.PIPE)
            brand, err = outInfo.communicate()
            return brand
        except:
            self.log.error("device_handle.py, getBrand : devices disconnect")
            exit(1)

    # 获取巡行的进程
    def getProcess(self):
        adbOutProcess = []
        outInfo = subprocess.Popen('adb shell ps com.Nrush.forensictool', shell=True, stdout=subprocess.PIPE)
        out, err = outInfo.communicate()
        for line in out.splitlines():
            adbOutProcess.append(line)
        try:
            if adbOutProcess[3]:
                return True
        except:
            return False


    #获取安装apk列表
    def get_apk_install(self):
        try :
            outInfo = subprocess.Popen('adb shell pm list packages com.Nrush.forensictool', shell=True, stdout=subprocess.PIPE)
            out, err = outInfo.communicate()
            return out
        except:
            self.log.error("device_handle.py, get_apk_install : devices disconnect")
            exit(1)
    #启动
    def activity_app(self):
        try:
            subprocess.Popen('adb shell am start -n com.Nrush.forensictool/.MainActivity', shell=True, stdout=subprocess.PIPE)
        except:
            self.log.error("device_handle.py, activity_app : devices disconnect")
            exit(1)

    #获取手机系统版本
    def getRelease(self):
        adbOutRelease = []
        outInfo = subprocess.Popen('adb shell getprop ro.build.version.release', shell=True, stdout=subprocess.PIPE)
        out, err = outInfo.communicate()
        for line in out.splitlines():
            adbOutRelease.append(line)

        release = adbOutRelease[0]
        return release

    # 检查是否连接成功
    def test_device_connect(self):
        try:
            outInfo = subprocess.Popen('adb get-serialno', shell=True, stdout=subprocess.PIPE)
            out, err = outInfo.communicate()

            if out:
                return True  # 连接成功
            else:
                log = Logger()
                log.error("device_handle.py, test_device_connect : no devices found")
                exit(1)

        except Exception:
            #print e #此处需要打印log
            exit(1)


if __name__ == '__main__':
    s = DeviceHandle()
    print(s.getBrand())



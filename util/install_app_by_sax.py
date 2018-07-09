# -*- coding: UTF-8 -*-

import re
import os
import time
import subprocess
import xml.sax

from util.log import Logger

pattern = re.compile(r"\d+")
attributes_result = {}
class Element(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.button_coord_and_id = []


    @classmethod
    def get_uidump(self):
        '''
        获取当前Activity控制树
        '''
        temp_parent_path = os.getcwd()
        xml_path_parent = temp_parent_path + '\\temp'
        if (os.path.exists(xml_path_parent) == False):
            os.makedirs(xml_path_parent)
        xml_path = xml_path_parent + '\\uidump.xml'

        #time_start = time.clock()
        try:
            run_command = "adb pull /data/local/tmp/uidump.xml {path}".format(path=xml_path)
            os.popen("adb shell uiautomator dump /data/local/tmp/uidump.xml")
            os.popen(run_command)
        except:
            log = Logger()
            log.error("install_app_by_sax.py, get_uidump : xml can not pull")
            exit(1)
        #time_end = time.clock()
        #time_cost2 = (time_end - time_start)
        #print "test_case2: ", time_cost2

    # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag

        try:
            if tag == "node":
                self.text = attributes["text"]
                self.className = attributes["class"]
                if self.text !="":
                    self.bounds = attributes["bounds"]
                    coord = pattern.findall(self.bounds)
                    Xpoint = (int(coord[2]) - int(coord[0])) / 2.0 + int(coord[0])
                    Ypoint = (int(coord[3]) - int(coord[1])) / 2.0 + int(coord[1])
                    self.button_coord_and_id.append(Xpoint)
                    self.button_coord_and_id.append(Ypoint)
                    attributes_result[self.text] = self.button_coord_and_id
                    self.button_coord_and_id = []

                if self.className == 'android.widget.CheckBox':
                    self.bounds = attributes["bounds"]
                    coord = pattern.findall(self.bounds)
                    Xpoint = (int(coord[2]) - int(coord[0])) / 2.0 + int(coord[0])
                    Ypoint = (int(coord[3]) - int(coord[1])) / 2.0 + int(coord[1])
                    self.button_coord_and_id.append(Xpoint)
                    self.button_coord_and_id.append(Ypoint)
                    attributes_result[self.className] = self.button_coord_and_id
                    self.button_coord_and_id = []
        except:
            print "install_app_by_sax error"
            exit(1)


    def end_element(self,name):
        pass
    #char_data函数
    def char_data(self,text):
        pass

    @classmethod
    def findElementAllText(self):
        temp_parent_path = os.getcwd()
        xml_path = temp_parent_path + '\\temp\\uidump.xml'

        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        Handler = Element()
        parser.setContentHandler(Handler)
        parser.parse(xml_path)

        return attributes_result

class Event(object):
    def __init__(self):
        subprocess.Popen("adb wait-for-device ")

    def touch(self, dx, dy):
        """
        触摸事件
        usage: touch(500, 500)
        """
        subprocess.Popen("adb shell input tap " + str(dx) + " " + str(dy))
        time.sleep(0.5)

#if (__name__ == "__main__"):
   # print(Element.findElementAllText())


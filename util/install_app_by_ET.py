# -*- coding: utf-8 -*-

import os
import re
import xml.etree.cElementTree as ET
import time

class Element(object):
   '''
   通过元素定位，需要Android 4.0以上
   '''
   def __init__(self):
      '''
      初始化，获取系统临时文件存储目录，定义匹配数字模式
      '''
      self.pattern = re.compile(r"\d+")

   def __uidump(self):
       '''
       获取当前Activity控制树
       '''
       temp_parent_path = os.getcwd()
       xml_path_parent = temp_parent_path + '\\temp'
       if(os.path.exists(xml_path_parent) == False):
           os.makedirs(xml_path_parent)

       time_start = time.clock()

       xml_path = xml_path_parent + '\\uidump.xml'
       run_command = "adb pull /data/local/tmp/uidump.xml {path}".format(path = xml_path)
       os.popen("adb shell uiautomator dump /data/local/tmp/uidump.xml")
       os.popen(run_command)


       time_end = time.clock()
       time_cost2 = (time_end - time_start)
       print "test_case2: ", time_cost2



   def __text_element(self):
       '''
       同属性单个元素，返回单个坐标元组
       :param attrib:
       :param name:
       :return:
       '''
       attributes_result = {} #返回{text:[323.0, 232.3]}的字典
       button_coord_and_id = []
       self.__uidump()
       temp_parent_path = os.getcwd()
       xml_path = temp_parent_path + '\\temp\\uidump.xml'
       tree = ET.ElementTree(file=xml_path)
       treeIter = tree.iter(tag='node')
       for elem in treeIter:
           if elem.attrib["text"] != "":
               text = elem.attrib["text"]
               bounds = elem.attrib['bounds']
               coord = self.pattern.findall(bounds)
               Xpoint = (int(coord[2]) - int(coord[0])) / 2.0 + int(coord[0])
               Ypoint = (int(coord[3]) - int(coord[1])) / 2.0 + int(coord[1])
               button_coord_and_id.append(Xpoint)
               button_coord_and_id.append(Ypoint)
               attributes_result[text] = button_coord_and_id
               button_coord_and_id = []

           if elem.attrib["className"] == 'android.widget.CheckBox':
               className = elem.attrib["className"]
               bounds = elem.attrib["bounds"]
               coord = self.pattern.findall(self.bounds)
               Xpoint = (int(coord[2]) - int(coord[0])) / 2.0 + int(coord[0])
               Ypoint = (int(coord[3]) - int(coord[1])) / 2.0 + int(coord[1])
               button_coord_and_id.append(Xpoint)
               button_coord_and_id.append(Ypoint)
               attributes_result[className] = button_coord_and_id
               button_coord_and_id = []
       return attributes_result

   def findElementAllText(self):
       """
       通过元素名称定位
       usage: findElementByName(u"相机")
       """
       return self.__text_element()

class Event(object):
    def __init__(self):
        os.popen("adb wait-for-device ")

    def touch(self, dx, dy):
        """
        触摸事件
        usage: touch(500, 500)
        """
        os.popen("adb shell input tap " + str(dx) + " " + str(dy))
        time.sleep(0.5)

'''
if __name__ == '__main__':
    re = Element()
    print(re.findElementAllText())

'''

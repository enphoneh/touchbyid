#!/usr/bin/python  
#encoding:utf-8
#encoding=gbk


'''
Created on 2014年11月11日

@author: EnphoneH
'''

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer


device = MonkeyRunner.waitForConnection()
easy_device = EasyMonkeyDevice(device)  #init easymonkeydevice object must start activity at first.Because the init method
hierarchyviewer = device.getHierarchyViewer()
#menu = hierarchyviewer.findViewByid('id/Menu_button')

for j in range(0,10000):
    easy_device.touch(By.id('id/Menu_button'),MonkeyDevice.DOWN_AND_UP)
    print("点击:" + str(j) + "次")
    MonkeyRunner.sleep(3)

# coding:utf-8

# @Author: Duanxiaogang
# @File :fail.py
# @DATE :2022/10/26

import time
import unittest
import os
from framework.logger import Loggoer   # 导入日志模块代码
from framework.get_devices import GetAdbDevice  # 导入设备获取类

logger = Loggoer(logger="Figure").getlogger()  # 获取Logger工厂类的方法
dut = GetAdbDevice()
device = dut.get_device()

now = time.strftime("%y%m%d%H%M%S",time.localtime())


class Failed(unittest.TestCase):
    def failed_test(self,error_info):
        logger.error("执行出错！")
        now = time.strftime("%y%m%d%H%M%S", time.localtime())
        report_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        pic = report_path + now + 'error.jpg'
        device.screenshot(pic)
        time.sleep(1)
        flag = False
        self.assertTrue(flag, msg=error_info)






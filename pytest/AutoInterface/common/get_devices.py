# coding： utf-8

# @Author: Duanxiaogang
# @File :get_devices.py
# @DATE :2022/10/27

import os
import re
from conf.logger import Logger
import uiautomator2 as u2
logger = Logger(logger="log_msg").getlogger()


class GetAdbDevice(object):

    def __init__(self):
        '''
            进行设备连接
        '''

        device_info = os.popen('adb devices').readlines()
        if len(device_info) <= 2:
            logger.info("未连接上设备\n")
        else:
            logger.info("已连上设备，sn如下：\n")
            for info in device_info:
                if info == 'STS40X190060\tdevice\n':
                    sn = re.findall(r'(.*)\tdevice', info)
                    SN = ''.join(i for i in sn)  # 去除括号
                    logger.info(SN)

                    self.SN = SN

    def get_device(self):
        device = u2.connect(self.SN)
        return device

# coding： utf-8

# @Author: Duanxiaogang
# @File :storage.py
# @DATE :2022/10/31
import os,re
import time
import unittest
from framework.logger import Loggoer
from framework.get_devices import GetAdbDevice
from framework.fail import Failed


logger = Loggoer(logger="Figure").getlogger()
dut = GetAdbDevice()
device = dut.get_device()


class Storage(unittest.TestCase):
    def ufsRW_test(self):
        logger.info("开始测试存储ufs读写")
        file_path = '../config/test.txt'
        logger.info(file_path)
        os.system("adb push "+file_path+" /sdcard/tmp/")
        time.sleep(1)
        file_info = os.popen('adb shell ls /sdcard/tmp/').read()
        if file_info.__contains__('test.txt'):
            logger.info("文件存储成功")
        else:
            error_info = "文件push失败"
            Failed.failed_test(self, error_info)

        os.system("adb pull /sdcard/tmp/test.txt ../testimg/1.txt")
        time.sleep(1)
        if os.path.exists('../config/1.txt'):
            logger.info("文件拉取本地成功")
        else:
            error_info = "文件拉取失败"
            Failed.failed_test(self, error_info)
        logger.info("删除测试文件")
        os.remove("../config/1.txt")

    def ufsRM_test(self):
        logger.info("开始测试存储ufs删除")
        os.system("adb shell rm -rf /sdcard/tmp/test.txt")
        time.sleep(1)
        file_sinfo = os.popen('adb shell ls /sdcard/tmp/').read()
        if file_sinfo:
            error_info = logger.info("文件删除失败")
            Failed.failed_test(self, error_info)
        else:
            logger.info("文件删除成功")

    def MemoryShow_test(self):
        logger.info("开始测试内存查看")
        memory_info = os.popen("adb shell cat /proc/meminfo |findstr MemTotal").read()
        memory_data = ''.join(re.findall("\d+", memory_info))
        M = int(memory_data) / 1024 / 1024
        if 7 < M <= 8:
            logger.info("设备总内存为8G")
        else:
            error_info = "设备内存错误"
            Failed.failed_test(self, error_info)






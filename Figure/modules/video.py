# coding： utf-8

# @Author: Duanxiaogang
# @File :video.py
# @DATE :2022/11/4

import time
from framework.logger import Loggoer
from framework.get_devices import GetAdbDevice
from framework.fail import Failed
import unittest

logger = Loggoer(logger="Figure").getlogger()
dut = GetAdbDevice()
device = dut.get_device()


class Video(unittest.TestCase):
    def playvideo_test(self):
        logger.info("开始进行video播放测试")
        try:

            device.app_start("com.android.music", activity=".VideoBrowserActivity")
            device.implicitly_wait(3)
            logger.info("开始播放。。。")
            time.sleep(1)
            device.xpath('//*[@resource-id="android:id/text1"]').click()
            time.sleep(5)

        except Exception as e:
            error_info = logger.info(f"异常：{e}")
            Failed.failed_test(self,error_info)

    def clearvideo_test(self):
        logger.info("清理video测试环境")
        try:
            device.app_clear("com.android.gallery3d")
            device.app_clear("com.android.music")
        except Exception as e:
            error_info = logger.info(f"异常：{e}")
            Failed.failed_test(self, error_info)

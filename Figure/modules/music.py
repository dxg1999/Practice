# coding： utf-8

# @Author: Duanxiaogang
# @File :music.py
# @DATE :2022/10/27

import time
from framework.logger import Loggoer
from framework.get_devices import GetAdbDevice
from framework.fail import Failed
import unittest

logger = Loggoer(logger="Figure").getlogger()
dut = GetAdbDevice()
device = dut.get_device()


class Music(unittest.TestCase):

    def playmusic_test(self):
        logger.info("开始播放音乐")
        device.app_start('com.android.music')
        status = device.app_wait('com.android.music')  # 等待其运行
        device.implicitly_wait(5)
        if device(resourceId='com.android.permissioncontroller:id/grant_dialog').exists:    # 判断是否有首次进入的弹窗
            device(resourceId='com.android.permissioncontroller:id/permission_allow_button').click()
        device.implicitly_wait(1)
        device(resourceId='com.android.music:id/play_indicator').click()
        device.implicitly_wait(1)
        device.xpath("//android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]").click()
        time.sleep(10)
        if not status:
            Failed.failed_test(self)
        else:

            logger.info("测试完毕——清除数据")
            device.app_clear('com.android.music')



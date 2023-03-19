# coding： utf-8

# @Author: Duanxiaogang
# @File :settings.py
# @DATE :2022/12/13

import time
from framework.logger import Loggoer
from framework.get_devices import GetAdbDevice
from framework.fail import Failed
import unittest

logger = Loggoer(logger="Figure").getlogger()
dut = GetAdbDevice()
device = dut.get_device()


class Settings(unittest.TestCase):
    def autolight(self):
        logger.info("开始调节自动背光")
        device.swipe(0.5, 0.014, 0.5, 0.385)
        device.implicitly_wait(5)

        device.xpath('//*[@resource-id="com.android.systemui:id/auto_switch"]').click()
        logger.info("自动背光按钮已点击")
        device.press("home")

    def ScreenSettings(self):
        try:
            logger.info("开始设置屏保时间")
            device.app_start("com.android.settings")
            device.implicitly_wait(5)
            device(scrollable=True).scroll.to(text="显示")
            device(resourceId="android:id/title", text="显示").click()
            device.implicitly_wait(1)
            device.shell("input keyevent 20")   # 向下操作
            device.shell("input keyevent 20")
            device.shell("input keyevent 20")
            device.xpath('//*[@text="屏保"]').click()
            device.implicitly_wait(3)
            device.xpath('//*[@text="启用时机"]').click()
            device.implicitly_wait(3)
            device.xpath('//*[@text="5 分钟"]').click()
            logger.info("已设置屏保为5分钟")
        except Exception as e:
            logger.error(e)

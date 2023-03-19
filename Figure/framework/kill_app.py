# coding： utf-8

# @Author: Duanxiaogang
# @File :kill_app.py
# @DATE :2022/11/15

import unittest
import time
from framework.get_devices import GetAdbDevice

device = GetAdbDevice().get_device()


class KillApp(unittest.TestCase):
    def clearapp_test(self):
        device.shell("input keyevent 187")
        device.implicitly_wait(3)
        device.xpath('//*[@resource-id="com.android.launcher3:id/clear_all_iv"]').click()
        time.sleep(1)
        device.press("home")


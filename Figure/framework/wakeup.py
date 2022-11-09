# coding： utf-8

# @Author: Duanxiaogang
# @File :wakeup.py
# @DATE :2022/10/27


import unittest
from framework.logger import Loggoer
from framework.get_devices import GetAdbDevice

logger = Loggoer(logger="Figure").getlogger()
dut = GetAdbDevice()
device = dut.get_device()


def wakeup_test():
    screen_status = device.info.get('screenOn')
    if screen_status is False:
        logger.info("设备熄屏中，开始唤醒")
        device.screen_on()
    else:
        pass


class WakeUp(unittest.TestCase):

    def unlock_test(self):
        wakeup_test()
        device.implicitly_wait(10)
        if device(className="android.view.ViewGroup").exists:  # 判断锁屏状态
            logger.info("处于非锁屏状态")
        else:
            logger.info("处于锁屏状态,开始解锁")
            device.press('home')

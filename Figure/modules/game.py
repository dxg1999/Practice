# coding： utf-8

# @Author: Duanxiaogang
# @File :game.py
# @DATE :2022/11/4
import time
from framework.logger import Loggoer
from framework.get_devices import GetAdbDevice
import unittest

logger = Loggoer(logger="Figure").getlogger()
dut = GetAdbDevice()
device = dut.get_device()


class Game(unittest.TestCase):

    def GameRunning_test(self):
        logger.info("打开游戏应用")
        device.app_start("com.tykj.bubble.uc")
        time.sleep(5)

    def GameClear_test(self):
        logger.info("关闭游戏应用")
        device.app_clear("com.tykj.bubble.uc")

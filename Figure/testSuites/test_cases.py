# coding： utf-8

# @Author: Duanxiaogang
# @File :test_cases.py
# @DATE :2022/10/27

import time
import os
import unittest
from framework.logger import Loggoer
from framework.get_devices import GetAdbDevice
from framework.wakeup import WakeUp
from modules.music import Music

logger = Loggoer(logger="Figure").getlogger()
dut = GetAdbDevice()
device = dut.get_device()


class Cases(unittest.TestCase):
    def setUp(self):
        logger.info("--------SetUp---------")

    def tearDown(self):
        # 移除监控
        logger.info("清理测试环境")
        device.watcher.remove()

    def test_music(self):
        WakeUp.unlock_test(self)
        logger.info("开始执行音乐类用例")
        Music.playmusic_test(self)


if __name__ == '__main__':
    unittest.main(verbosity=2)

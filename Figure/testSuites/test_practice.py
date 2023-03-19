# coding： utf-8

# @Author: Duanxiaogang
# @File :test_practice.py
# @DATE :2022/12/29

import time
import unittest
from framework.logger import Loggoer
from framework.get_devices import GetAdbDevice
from parameterized import parameterized
from modules.game import Game
from framework.kill_app import KillApp


logger = Loggoer(logger="Figure").getlogger()
dut = GetAdbDevice()
device = dut.get_device()


class Cases(unittest.TestCase):
    '''
    游戏专项测试。。。
    '''

    def setUp(self):
        logger.info("--------SetUp---------")

    def tearDown(self):
        # 移除监控
        logger.info("--------TearDown---------")

    @parameterized.expand([(i,) for i in range(1)])
    def test_T01_startgame(self, *args):
        """游戏王者测试"""
        logger.info("返回主界面，开始王者游戏测试")
        Game.GameStart_test(self)
        Game.GameSelect_test(self)
        Game.GameRunning_test(self)
        logger.info("关闭游戏应用")
        KillApp.clearapp_test(self)


if __name__ == '__main__':
    unittest.main(verbosity=2)

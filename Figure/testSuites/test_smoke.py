# coding： utf-8

# @Author: Duanxiaogang
# @File :test_smoke.py
# @DATE :2022/10/31

import unittest,random,time
from framework.logger import Loggoer
from framework.get_devices import GetAdbDevice
from framework.kill_app import KillApp
from framework.wakeup import WakeUp
from modules.dormancy import Dormancy
from modules.storage import Storage
from modules.bluetooth import BlueTooth
from modules.wifi import Wifi
from modules.settings import Settings
from modules.appwindow import App_Window_test
from parameterized import parameterized

logger = Loggoer(logger="Figure").getlogger()
dut = GetAdbDevice()
device = dut.get_device()


class Cases(unittest.TestCase):
    '''
    冒烟测试。。。
    '''

    def setUp(self):
        logger.info("--------SetUp---------")

    def tearDown(self):
        # 移除监控
        logger.info("--------TearDown---------")
        KillApp.clearapp_test(self)

    def test_T01_dormancy(self):
        """主动休眠测试"""
        logger.info("返回主界面，开始进行1min休眠测试")
        Dormancy.Active_dormancy_test(self)
        logger.info("清理测试环境")
        WakeUp.unlock_test(self)

    def test_T02_storage(self):
        """Storage的三个测试"""
        logger.info("开始执行storage类用例")
        Storage.ufsRW_test(self)
        Storage.ufsRM_test(self)
        Storage.MemoryShow_test(self)

    def test_T03_bluetooth(self):
        """蓝牙配对连接测试"""
        BlueTooth.connectBT_test(self)
        BlueTooth.palymusic_test(self)

    def test_T04_wifi(self):
        """连接wifi测试"""
        name4G = "H3C_350304"
        Wifi.wifi_connect_test(self,name4G)
        Wifi.off_wifi_test(self)
        name5G = "H3C_350304_5G"
        Wifi.wifi_connect_test(self,name5G)
        Wifi.off_wifi_test(self)

    def test_T05_light(self):
        """自动背光功能侧测试"""
        Settings.autolight(self)

    def test_T06_screen(self):
        """屏保设置功能侧测试"""
        Settings.ScreenSettings(self)


if __name__ == '__main__':
    unittest.main(verbosity=2)
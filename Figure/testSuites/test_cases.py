# coding： utf-8

# @Author: Duanxiaogang
# @File :test_cases.py
# @DATE :2022/10/31

import unittest,random,time
from framework.logger import Loggoer
from framework.get_devices import GetAdbDevice
from framework.ClearData import Clear_Data
from framework.wakeup import WakeUp
from framework.kill_app import KillApp
from modules.dormancy import Dormancy
from modules.storage import Storage
from modules.bluetooth import BlueTooth
from modules.wifi import Wifi
from modules.video import Video
from modules.game import Game
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
        # device.watcher.remove()

    @parameterized.expand([(i,) for i in range(2)])
    def test_dormancyVideo(self, *args):
        logger.info("开始执行播放视频时——屏保休眠类用例")
        Video.playvideo_test(self)
        app_num = random.randint(2, 4)

        if app_num == 2:
            Dormancy.PassiveSleep_test(self)
        elif app_num == 3:
            Dormancy.Power_ScreenOff_test(self)
        elif app_num == 4:
            Dormancy.Passive_ScreenOff_test(self)
        Video.clearvideo_test(self)

    @parameterized.expand([(i,) for i in range(2)])
    def test_dormancyGame(self, *args):
        logger.info("开始执行玩游戏时——屏保休眠类用例")
        Game.GameRunning_test(self)
        app_num = random.randint(2, 4)
        # 删除主动进入休眠的场景
        if app_num == 2:
            Dormancy.PassiveSleep_test(self)
        elif app_num == 3:
            Dormancy.Power_ScreenOff_test(self)
        elif app_num == 4:
            Dormancy.Passive_ScreenOff_test(self)
        Game.GameClear_test(self)

    @parameterized.expand([(i,) for i in range(2)])
    def test_dormancyWB(self, *args):
        logger.info("开始执行wifi蓝牙时——屏保休眠类用例")
        # BlueTooth.connectBT_test(self)
        Wifi.wifi_connect_test(self)
        time.sleep(1)
        Wifi.off_wifi_test(self)
        time.sleep(1)
        Wifi.reconnect_wifi_test(self)
        app_num = random.randint(1, 4)
        if app_num == 1:
            Dormancy.ActiveSleep_test(self)
        elif app_num == 2:
            Dormancy.PassiveSleep_test(self)
        elif app_num == 3:
            Dormancy.Power_ScreenOff_test(self)
        elif app_num == 4:
            Dormancy.Passive_ScreenOff_test(self)
        Clear_Data.clearWB(self)

    # 通过 Parameterized 实现参数化
    @parameterized.expand([(i,) for i in range(2)])
    def test_AppSmallWindow(self, *args):
        logger.info("开始执行小窗切换类用例")
        App_Window_test.smallwindow_test(self)
        KillApp.clearapp_test(self)

    # 通过 Parameterized 实现参数化
    @parameterized.expand([(i,) for i in range(2)])
    def test_storage(self, *args):
        WakeUp.unlock_test(self)
        logger.info("开始执行storage类用例")
        Storage.ufsRW_test(self)
        Storage.ufsRM_test(self)
        Storage.MemoryShow_test(self)

    # def test_bluetooth(self):
    #     WakeUp.unlock_test(self)
    #     logger.info("开始执行bluetooth类用例")
    #     for i in range(10):
    #         BlueTooth.reconnect_test(self)
    #         BlueTooth.offBT_test(self)

    # def test_reconnectwifi(self):
    #     Wifi.reconnect_wifi_test(self)
    #     Wifi.off_wifi_test(self)


if __name__ == '__main__':
    unittest.main(verbosity=2)

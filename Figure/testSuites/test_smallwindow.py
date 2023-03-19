# coding： utf-8

# @Author: Duanxiaogang
# @File :test_smallwindow.py
# @DATE :2022/11/14
import time
import unittest
from framework.logger import Loggoer
from framework.get_devices import GetAdbDevice
from framework.kill_app import KillApp
from modules.wifi import Wifi
from modules.appwindow import App_Window_test
from parameterized import parameterized

logger = Loggoer(logger="Figure").getlogger()
dut = GetAdbDevice()
device = dut.get_device()


class Cases(unittest.TestCase):
    '''
    小窗测试。。。
    '''

    def setUp(self):
        logger.info("--------SetUp---------")

    def tearDown(self):
        logger.info("--------TearDown---------")
        # KillApp.clearapp_test(self)
        time.sleep(1)

    # @parameterized.expand([(i,) for i in range(1)])
    # def test_T01_StartSmallWindow(self,*args):
    #     logger.info("开始执行小窗用例")
    #     App_Window_test.sw_Start_test(self)
    #     time.sleep(1)
    #     App_Window_test.sw_MoveLocation_test(self)
    #     time.sleep(1)
    #     App_Window_test.sw_ChangeStatus_test(self)

    def test_T02_ChoiceSmallWindow(self):
        num = App_Window_test.sw_Start_test(self)
        globals()["app"] = num

    @parameterized.expand([(i,) for i in range(50)])
    def test_T03_RepeatSmallWindow(self, *args):
        num = globals()["app"]
        time.sleep(1)
        App_Window_test.sw_RepeatStart_test(self, choice_num=num)


if __name__ == '__main__':
    unittest.main(verbosity=2)




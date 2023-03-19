# coding： utf-8

# @Author: Duanxiaogang
# @File :test_appsmall.py
# @DATE :2022/11/29

import pytest
import time
import allure
from conf.logger import Logger
from common.kill_app import KillApp
from module.appwindow import App_Window_test
logger = Logger(logger="log_msg").getlogger()


def setup_function():
    logger.info("--------SetUp---------")


def teardown_function():
    logger.info("--------TearDown---------")
    KillApp.clearapp_test()
    time.sleep(1)


# @pytest.mark.parametrize('in_data', eval(re_data), ids=[i['detail'] for i in TestData])
@allure.feature("小窗测试模块")
class Test_Case():
    @allure.feature("小窗mini模式移动")
    @pytest.mark.repeat(3)
    def test_StartSmallWindow(self, *args):
        logger.info("开始执行小窗切换类用例")

        with allure.step("打开应用的小窗"):
            App_Window_test.sw_Start_test(self)
            time.sleep(1)
        with allure.step("移动小窗"):
            App_Window_test.sw_MoveLocation_test(self)
            time.sleep(1)
        with allure.step("切换小窗形态"):
            App_Window_test.sw_ChangeStatus_test(self)


if __name__ == '__main__':
    pytest.main(['-v', '-s', "test_appsamll.py"])

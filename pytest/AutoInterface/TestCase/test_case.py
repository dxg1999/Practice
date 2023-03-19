# coding： utf-8

# @Author: Duanxiaogang
# @File :test_case.py
# @DATE :2022/12/19
import pytest
import time
import allure
from conf.logger import Logger
from common.kill_app import KillApp
from module.settings import Settings
logger = Logger(logger="log_msg").getlogger()


# @pytest.mark.parametrize('in_data', eval(re_data), ids=[i['detail'] for i in TestData])
@allure.feature("设置模块")
class Test_Case():

    def setup(self):
        logger.info("--------SetUp---------")

    def teardown(self):
        logger.info("--------TearDown---------")
        KillApp.clearapp_test(self)

    # @allure.title("wifi相关功能按钮连点测试")
    # @pytest.mark.repeat(1)
    # def test_T01_wifi_click_btn(self, *args):
    #     Settings.setting_wifi_btn(self)

    # @allure.title("蓝牙相关功能按钮连点测试")
    # @pytest.mark.repeat(1)
    # def test_T02_bluetooth_click_btn(self, *args):
    #     Settings.setting_bluetooth_btn(self)

    # @allure.title("应用相关功能按钮连点测试")
    # @pytest.mark.repeat(1)
    # def test_T03_app_click_btn(self, *args):
    #     Settings.setting_app_btn(self)

    # @allure.title("通知相关功能按钮连点测试")
    # @pytest.mark.repeat(1)
    # def test_T04_notice_click_btn(self, *args):
    #     Settings.setting_notice_btn(self)

    @allure.title("显示相关功能按钮连点测试")
    @pytest.mark.repeat(1)
    def test_T05_display_click_btn(self, *args):
        Settings.setting_display_btn(self)

    # @allure.title("隐私相关功能按钮连点测试")
    # @pytest.mark.repeat(1)
    # def test_T06_secret_click_btn(self, *args):
    #     Settings.setting_secret_btn(self)
    #
    # @allure.title("系统相关功能按钮连点测试")
    # @pytest.mark.repeat(1)
    # def test_T07_system_click_btn(self, *args):
    #     Settings.setting_system_btn(self)
    #
    # @allure.title("游戏模式相关功能按钮连点测试")
    # @pytest.mark.repeat(1)
    # def test_T08_game_click_btn(self, *args):
    #     Settings.setting_game_btn(self)


if __name__ == '__main__':
    pytest.main(['-v', '-s', "test_appsamll.py"])

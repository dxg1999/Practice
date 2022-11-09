# coding： utf-8

# @Author: Duanxiaogang
# @File :wifi.py
# @DATE :2022/10/27
import os
import time
from framework.logger import Loggoer
from framework.get_devices import GetAdbDevice
from framework.fail import Failed
import unittest

logger = Loggoer(logger="Figure").getlogger()
dut = GetAdbDevice()
device = dut.get_device()


class Wifi(unittest.TestCase):

    def wifi_connect_test(self):
        logger.info("开始wifi连接测试")
        wifi_status = os.popen("adb shell settings get global wifi_on").readlines()
        if wifi_status == ['1\n']:
            logger.info('WIFI已经开启')
        elif wifi_status == ['0\n']:
            logger.info('WIFI已经关闭,开始开启')
            os.popen('adb shell svc wifi enable')
        else:
            logger.info('WIFI Error')
        time.sleep(1)
        device.app_start("com.android.settings")
        device.implicitly_wait(3)
        device.xpath('//*[@text="网络和互联网"]').click()
        device.implicitly_wait(3)
        device.xpath('//*[@text="WLAN"]').click()
        device.implicitly_wait(5)
        time.sleep(1)
        device.xpath('//*[@text="H3C_350304"]').click()
        # 需切换为源生英文键盘
        time.sleep(2)
        logger.info("输入wifi密钥")
        os.system('adb shell input text 12345678')
        device.implicitly_wait(3)
        device.xpath('//*[@resource-id="android:id/button1"]').click()
        time.sleep(5)
        if device(resourceId="android:id/summary", text="已连接").exists:
            logger.info("wifi连接成功")
        else:
            logger.info("Wifi连接失败")
            Failed.failed_test(self)

    def off_wifi_test(self):

        wifi_status = os.popen("adb shell settings get global wifi_on").readlines()
        if wifi_status == ['1\n']:
            logger.info('WIFI已经开启,开始关闭')
            os.popen('adb shell svc wifi disable')
        elif wifi_status == ['0\n']:
            logger.info('WIFI已经关闭')
        else:
            logger.info('WIFI Error')
        time.sleep(1)

    def reconnect_wifi_test(self):
        logger.info("开启wifi")
        os.popen('adb shell svc wifi enable')
        time.sleep(1)
        device.app_start("com.android.settings")
        device.implicitly_wait(3)
        device.xpath('//*[@text="网络和互联网"]').click()
        device.implicitly_wait(3)
        device.xpath('//*[@text="WLAN"]').click()
        device.implicitly_wait(10)
        if device(resourceId="android:id/summary", text="已连接").exists:
            logger.info("wifi重连成功")
        else:
            logger.info("Wifi重连失败")
            Failed.failed_test(self)


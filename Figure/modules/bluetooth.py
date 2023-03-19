# coding： utf-8

# @Author: Duanxiaogang
# @File :bluetooth.py
# @DATE :2022/10/31
import os
import time
from framework.logger import Loggoer
from framework.get_devices import GetAdbDevice
from framework.fail import Failed
import unittest

logger = Loggoer(logger="Figure").getlogger()
dut = GetAdbDevice()
device = dut.get_device()


class BlueTooth(unittest.TestCase):

    def connectBT_test(self):
        logger.info("开始测试蓝牙连接")
        time.sleep(1)
        bt_status = os.popen("adb shell settings get global bluetooth_on").readlines()
        if bt_status == ['1\n']:
            logger.info("蓝牙已开启")
        else:
            logger.info("正在打开蓝牙")
            os.popen("adb shell svc bluetooth enable")
            time.sleep(1)
        # 打开设置中心
        device.app_start("com.android.settings")
        device.implicitly_wait(3)
        device.xpath('//*[@text="已连接的设备"]').click()
        device.implicitly_wait(3)
        device.xpath('//*[@text="与新设备配对"]').click()
        device.implicitly_wait(10)
        device.xpath('//*[@text="OPPO Enco W51"]').click()
        device.implicitly_wait(10)
        device(resourceId="android:id/button1").click()
        logger.info("进行蓝牙配对")
        device.implicitly_wait(10)
        if device(resourceId="android:id/title", text="媒体设备").exists(timeout=2):
            logger.info("配对成功")
        else:
            error_info = logger.info("蓝牙配对失败")
            Failed.failed_test(self,error_info)

    def offBT_test(self):
        bt_status = os.popen("adb shell settings get global bluetooth_on").readlines()
        if bt_status == ['1\n']:
            logger.info("蓝牙已开启,正在关闭")
            os.popen("adb shell svc bluetooth disable")
        else:
            logger.info("蓝牙已关闭")
        time.sleep(1)


    def reconnect_test(self):
        time.sleep(1)
        bt_status = os.popen("adb shell settings get global bluetooth_on").readlines()
        if bt_status == ['1\n']:
            logger.info("蓝牙已开启")
        else:
            logger.info("正在打开蓝牙")
            os.popen("adb shell svc bluetooth enable")
            time.sleep(1)
        # 打开设置中心
        device.app_start("com.android.settings")
        device.implicitly_wait(3)
        device.xpath('//*[@text="已连接的设备"]').click()
        device.implicitly_wait(10)
        if device(resourceId="android:id/title", text="媒体设备").exists(timeout=2):
            logger.info("连接成功")
        else:
            error_info = logger.info("蓝牙连接失败")
            Failed.failed_test(self, error_info)
        device.app_stop("com.android.settings")
        device.press("home")


    def palymusic_test(self):
        try:
            file_path = "../config/bird.mp3"
            logger.info("存储mp3文件到sdcard")
            os.system("adb push " + file_path + " /sdcard/Download/")
            time.sleep(1)
            device.app_start('com.android.music')
            status = device.app_wait('com.android.music')  # 等待其运行
            device.implicitly_wait(5)
            if device(resourceId='com.android.permissioncontroller:id/grant_dialog').exists:  # 判断是否有首次进入的弹窗
                device(resourceId='com.android.permissioncontroller:id/permission_allow_button').click()
            device.implicitly_wait(1)
            time.sleep(5)
            device.app_clear("com.android.documentsui")
            logger.info("蓝牙播放音乐测试——成功结束")

        except Exception as e:
            error_info = logger.info(f"异常：{e}")
            Failed.failed_test(self, error_info)

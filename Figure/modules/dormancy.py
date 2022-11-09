# coding： utf-8

# @Author: Duanxiaogang
# @File :dormancy.py
# @DATE :2022/10/31
import random
import time,os
from framework.logger import Loggoer
from framework.get_devices import GetAdbDevice
from framework.fail import Failed
import unittest

logger = Loggoer(logger="Figure").getlogger()
dut = GetAdbDevice()
device = dut.get_device()

def set_clock():
    device.app_start("com.android.deskclock")
    device.implicitly_wait(3)
    device(resourceId="android:id/text1").click()
    device.implicitly_wait(3)
    device(resourceId="com.android.deskclock:id/fab").click()
    time.sleep(1)
    h = int(device(resourceId="android:id/hours").get_text())
    m = int(device(resourceId="android:id/minutes").get_text())

    #print(h, m)
    if (m + 2) >= 60:
        h = h + 1
        m = (m + 2) - 60
    else:
        m = m + 2
    if h < 10:
        if m < 10:
            logger.info(f"设置闹钟{h}:{m}")
            os.popen("adb shell input text {}{}".format("0" + str(h), "0" + str(m)))
        else:
            logger.info(f"设置闹钟{h}:{m}")
            os.popen("adb shell input text {}{}".format("0" + str(h), str(m)))
    else:
        if m < 10:
            logger.info(f"设置闹钟{h}:{m}")
            os.popen("adb shell input text {}{}".format(str(h), "0" + str(m)))
        else:
            logger.info(f"设置闹钟{h}:{m}")
            os.popen("adb shell input text {}{}".format(str(h), str(m)))
    time.sleep(1)
    device(resourceId="android:id/button1").click()



class Dormancy(unittest.TestCase):

    def ActiveSleep_test(self):

        num = random.randint(1, 2)
        if num == 1:
            logger.info("自动休眠进入屏保")
            time.sleep(60)
            logger.info("进行手动点击唤醒")
            device.press('home')
            if device(className="android.view.ViewGroup").exists(timeout=5):  # 判断锁屏状态
                logger.info("屏保点击唤醒成功")
            else:
                Failed.failed_test(self)

        elif num == 2:
            logger.info("设置闹钟唤醒")
            set_clock()
            logger.info("自动休眠进入屏保")
            time.sleep(120)
            if device(resourceId="com.android.deskclock:id/alarm").exists(timeout=5):
                logger.info("闹钟唤醒屏保成功")
                device.app_clear("com.android.deskclock")

            else:
                Failed.failed_test(self)

    def PassiveSleep_test(self):

        num = random.randint(1, 2)
        if num == 1:
            logger.info("手动休眠进入屏保")
            device.swipe(0.5, 0.014, 0.5, 0.385)
            device.swipe(0.5, 0.014, 0.5, 0.385)
            device.implicitly_wait(5)
            device(resourceId="com.android.systemui:id/pm_lite_saverscreen").click()  # 屏保按钮
            time.sleep(5)
            logger.info("进行手动点击唤醒")
            device.press('home')
            if device(className="android.view.ViewGroup").exists(timeout=5):  # 判断锁屏状态
                logger.info("屏保点击唤醒成功")
            else:
                Failed.failed_test(self)

        elif num == 2:
            logger.info("设置闹钟唤醒")
            set_clock()
            logger.info("手动休眠进入屏保")
            device.swipe(0.5, 0.014, 0.5, 0.385)
            device.implicitly_wait(5)
            device(resourceId="com.android.systemui:id/pm_lite_saverscreen").click()  # 屏保按钮
            time.sleep(120)
            if device(resourceId="com.android.deskclock:id/alarm").exists(timeout=5):
                logger.info("闹钟唤醒屏保成功")
                device.app_clear("com.android.deskclock")

            else:
                Failed.failed_test(self)

    def Power_ScreenOff_test(self):
        num = random.randint(1, 2)
        if num == 1:
            logger.info("power键灭屏")
            device.press("power")
            time.sleep(5)
            logger.info("点击power键唤醒")
            device.press("power")
            screen_status = device.info.get('screenOn')
            if screen_status is True:
                logger.info("灭屏点击唤醒成功")

            else:
                Failed.failed_test(self)

        elif num == 2:
            logger.info("设置闹钟唤醒")
            set_clock()
            logger.info("power键灭屏")
            device.press("power")
            time.sleep(120)
            if device(resourceId="com.android.deskclock:id/alarm").exists(timeout=5):
                logger.info("灭屏闹钟唤醒成功")
                device.app_clear("com.android.deskclock")

            else:
                Failed.failed_test(self)

    def Passive_ScreenOff_test(self):
        num = random.randint(1, 2)
        if num == 1:
            logger.info("通知栏灭屏")
            device.swipe(0.5, 0.014, 0.5, 0.385)
            device.swipe(0.5, 0.014, 0.5, 0.385)
            device.implicitly_wait(5)
            device(resourceId="com.android.systemui:id/pm_lite_closescreen").click()  # 熄屏按钮
            time.sleep(5)
            logger.info("点击power键唤醒")
            device.press("power")
            screen_status = device.info.get('screenOn')
            if screen_status is True:
                logger.info("灭屏点击唤醒成功")

            else:
                Failed.failed_test(self)

        elif num == 2:
            logger.info("设置闹钟唤醒")
            set_clock()
            logger.info("通知栏灭屏")
            device.swipe(0.5, 0.014, 0.5, 0.385)
            device.implicitly_wait(5)
            device(resourceId="com.android.systemui:id/pm_lite_closescreen").click()  # 熄屏按钮
            time.sleep(120)
            if device(resourceId="com.android.deskclock:id/alarm").exists(timeout=5):
                logger.info("闹钟唤醒屏保成功")
                device.app_clear("com.android.deskclock")

            else:
                Failed.failed_test(self)


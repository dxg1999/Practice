# coding： utf-8

# @Author: Duanxiaogang
# @File :appwindow.py
# @DATE :2022/11/3
import time
import unittest
import random
from framework.logger import Loggoer
from framework.fail import Failed
from framework.get_devices import GetAdbDevice

logger = Loggoer(logger="Figure").getlogger()
dut = GetAdbDevice()
device = dut.get_device()


class App_Window_test(unittest.TestCase):
    def smallwindow_test(self):

        """
        长按图标进入
        device(text="Edge").long_click()
        device.implicitly_wait(3)
        device(resourceId="com.android.launcher3:id/bubble_text", text="小窗").click()
        """
        try:
            device.press("home")
            device.shell("input keyevent 187")
            device.implicitly_wait(3)
            logger.info("打开时钟应用的小窗模式")
            device(resourceId="com.android.launcher3:id/name_tv", text="时钟").click()
            time.sleep(2)
            device.xpath('//*[@resource-id="android:id/maximize_window"]').click()
            device.implicitly_wait(3)
            device.shell("input keyevent 187")
            device.implicitly_wait(3)
            logger.info("切换图库应用的小窗模式")
            device(resourceId="com.android.launcher3:id/name_tv", text="图库").click()
            time.sleep(2)
            device.click(0.098, 0.063)
            device.implicitly_wait(2)
            device.xpath('//*[@resource-id="android:id/maximize_window"]').click()
            device.implicitly_wait(3)
            device.shell("input keyevent 187")
            device.implicitly_wait(1)
            device.xpath('//*[@resource-id="com.android.launcher3:id/clear_all_iv"]').click()
            device.press("home")


            logger.info("开始连点通知栏的多种开关")
            device.swipe(0.5, 0.014, 0.5, 0.385)
            device.implicitly_wait(5)
            button_list = ["蓝牙","护眼模式","游戏模式","转储 SysUI 堆"]
            btn = random.choices(button_list)[0]
            logger.info(f"点击-{btn}")
            device(resourceId="com.android.systemui:id/tile_label", text=btn).click_gone(maxretry=10, interval=0.1)
            device.press("home")

            logger.info("开始settings的开关连点")
            device.app_start("com.android.settings")
            device.implicitly_wait(3)
            device.xpath('//*[@text="网络和互联网"]').click()
            device.implicitly_wait(3)
            device(resourceId="android:id/widget_frame").click_gone(maxretry=10, interval=0.1)
            device.implicitly_wait(1)
            device(scrollable=True).scroll.to(text="显示")
            device(resourceId="android:id/title", text="显示").click()
            device.implicitly_wait(1)
            device(resourceId='android:id/widget_frame')[0].click_gone(maxretry=10, interval=0.1)
            device.implicitly_wait(1)
            #device(scrollable=True).scroll.to(text="隐私")
            device(resourceId="android:id/title", text="隐私").click()
            device.implicitly_wait(1)
            device(resourceId='android:id/switch_widget')[0].click_gone(maxretry=10, interval=0.1)
            device.implicitly_wait(1)
            device(resourceId="android:id/title", text="游戏模式设置").click()
            device(resourceId="android:id/switch_widget").click_gone(maxretry=10, interval=0.1)



        except Exception as e:
            logger.info(f"异常：{e}")
            Failed.failed_test(self)




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
            logger.info("切换日历应用的小窗模式")
            device(resourceId="com.android.launcher3:id/name_tv", text="日历").click()
            time.sleep(2)
            device(resourceId="android:id/move_window").click()
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
            error_info = logger.info(f"异常：{e}")
            Failed.failed_test(self, error_info)

    def sw_Start_test(self):
        try:
            # App_list = ["时钟", "日历", "图库", "录音机", "文件", "音乐", "视频"]
            App_list = ["日历", "图库"]
            choice_num = random.choices(App_list)[0]
            if choice_num == "录音机":
                logger.info("长按应用图标——打开录音机的小窗")
                device(text="录音机").long_click()
                device.implicitly_wait(3)
                device(resourceId="com.android.launcher3:id/bubble_text", text="小窗").click()
                time.sleep(3)
                if device(resourceId="android:id/caption").exists:
                    logger.info("成功进入小窗模式")
                else:
                    logger.info("error")

            elif choice_num == "日历":
                logger.info("recent界面点击小窗的应用——打开日历的小窗")
                device.shell("input keyevent 187")
                device.implicitly_wait(3)

                device(resourceId="com.android.launcher3:id/name_tv", text="日历").click()
                time.sleep(3)
                if device(resourceId="android:id/caption").exists:
                    logger.info("成功进入小窗模式")
                else:
                    logger.info("error")

            elif choice_num == "时钟":
                logger.info("recent界面点击小窗的应用——打开时钟的小窗")
                device.shell("input keyevent 187")
                device.implicitly_wait(3)

                device(resourceId="com.android.launcher3:id/name_tv", text="时钟").click()
                time.sleep(3)
                if device(resourceId="android:id/caption").exists:
                    logger.info("成功进入小窗模式")
                else:
                    logger.info("error")

            elif choice_num == "音乐":
                logger.info("recent界面点击小窗的应用——打开音乐的小窗")
                device.shell("input keyevent 187")
                device.implicitly_wait(3)

                device(resourceId="com.android.launcher3:id/name_tv", text="音乐").click()
                time.sleep(3)
                if device(resourceId="android:id/caption").exists:
                    logger.info("成功进入小窗模式")
                else:
                    logger.info("error")

            elif choice_num == "图库":
                logger.info("recent界面点击小窗的应用——打开图库的小窗")
                device.shell("input keyevent 187")
                device.implicitly_wait(3)

                device(resourceId="com.android.launcher3:id/name_tv", text="图库").click()
                time.sleep(3)
                if device(resourceId="android:id/caption").exists:
                    logger.info("成功进入小窗模式")
                else:
                    logger.info("error")

            elif choice_num == "视频":
                logger.info("recent界面点击小窗的应用——打开视频的小窗")
                device.shell("input keyevent 187")
                device.implicitly_wait(3)

                device(resourceId="com.android.launcher3:id/name_tv", text="视频").click()
                time.sleep(3)
                if device(resourceId="android:id/caption").exists:
                    logger.info("成功进入小窗模式")
                else:
                    logger.info("error")

            elif choice_num == "文件":
                logger.info("recent界面点击应用卡片的小窗按钮——打开文件的小窗")
                device.app_start("com.android.documentsui",activity="com.android.documentsui.files.FilesActivity")
                device.implicitly_wait(3)
                device.shell("input keyevent 187")
                device.implicitly_wait(3)
                device(resourceId="com.android.launcher3:id/small_window_mark_iv").click()
                time.sleep(3)
                device(resourceId="android:id/move_window").click()
                time.sleep(1)
                if device(resourceId="android:id/caption").exists:
                    logger.info("成功进入小窗模式")
                else:
                    logger.info("error")

        except Exception as e:
            error_info = logger.info(f"异常：{e}")
            Failed.failed_test(self, error_info)

        return choice_num

    def sw_MoveLocation_test(self):
        try:
            device(resourceId="android:id/move_window").click()
            time.sleep(1)
            logger.info("进入mini小窗")
            # 小窗这个缩小按钮的布局跟实际不符，导致无法点击正确位置
            device(resourceId="android:id/mini_size_window").click()
            # device.click(90, 80)
            device.implicitly_wait(3)

            device.drag(0, 72, 2128, 72, 0.1)
            device.drag(2128, 72, 2128, 900, 0.1)
            device.drag(2128, 900, 0, 900, 0.1)
            device.drag(0, 900, 0, 72, 0.1)

            time.sleep(1)
            logger.info("小窗移动位置一圈完毕")

        except Exception as e:
            error_info = logger.info(f"异常：{e}")
            Failed.failed_test(self, error_info)

    def sw_RepeatStart_test(self,choice_num):
        """
        小窗mini模式，再次进入小窗
        """
        logger.info(f"重复进入{choice_num}小窗，验证小窗模式的大小和位置")
        try:
            if choice_num == "录音机":
                logger.info("长按应用图标——打开录音机的小窗")
                device(text="录音机").long_click()
                time.sleep(2)
                device(resourceId="com.android.launcher3:id/bubble_text", text="小窗").click()

            elif choice_num == "日历":
                logger.info("recent界面点击小窗的应用——打开日历的小窗")
                device.shell("input keyevent 187")
                time.sleep(2)
                device(resourceId="com.android.launcher3:id/name_tv", text="日历").click()

            elif choice_num == "时钟":
                logger.info("recent界面点击小窗的应用——打开时钟的小窗")
                device.shell("input keyevent 187")
                device.implicitly_wait(3)
                time.sleep(2)
                device(resourceId="com.android.launcher3:id/name_tv", text="时钟").click()

            elif choice_num == "音乐":
                logger.info("recent界面点击小窗的应用——打开音乐的小窗")
                device.shell("input keyevent 187")

                device(resourceId="com.android.launcher3:id/name_tv", text="音乐").click()

            elif choice_num == "图库":
                logger.info("recent界面点击小窗的应用——打开图库的小窗")
                device.shell("input keyevent 187")
                time.sleep(2)
                device(resourceId="com.android.launcher3:id/name_tv", text="图库").click()

            elif choice_num == "视频":
                logger.info("recent界面点击小窗的应用——打开视频的小窗")
                device.shell("input keyevent 187")
                time.sleep(2)
                device(resourceId="com.android.launcher3:id/name_tv", text="视频").click()

            elif choice_num == "文件":
                logger.info("recent界面点击应用卡片的小窗按钮——打开文件的小窗")
                device.app_start("com.android.documentsui",activity="com.android.documentsui.files.FilesActivity")
                device.implicitly_wait(3)
                device.shell("input keyevent 187")
                device.implicitly_wait(3)
                device(resourceId="com.android.launcher3:id/small_window_mark_iv").click()
        except Exception as e:
            error_info = logger.debug(f"异常：{e}")
            Failed.failed_test(self, error_info)

        time.sleep(3)
        device(resourceId="android:id/move_window").click()
        time.sleep(1)
        if device(resourceId="android:id/caption").exists:
            logger.info("成功进入小窗模式——且是正常状态的小窗")
        else:
            error_info = "error,未进入正常状态的小窗"
            Failed.failed_test(self, error_info)

    def sw_ChangeStatus_test(self):
        """
        小窗切换三种形态
        """
        device.click(140, 90)
        time.sleep(1)
        if device(resourceId="android:id/caption").exists:
            logger.info("切换为小窗——正常状态")
        else:
            logger.info("小窗状态切换异常")
        device.implicitly_wait(3)
        device.xpath('//*[@resource-id="android:id/maximize_window"]').click()
        device.implicitly_wait(3)
        if device(description="主屏幕").exists:
            error_info = logger.info("小窗状态切换全屏异常")
            Failed.failed_test(self,error_info)
        else:
            logger.info("切换为小窗——全屏状态")



# coding： utf-8

# @Author: Duanxiaogang
# @File :settings.py
# @DATE :2022/12/19
import time

from conf.logger import Logger
from common.Assert import AssertMethod
from common.get_devices import GetAdbDevice

logger = Logger(logger="log_msg").getlogger()
dut = GetAdbDevice()
device = dut.get_device()


class Settings():
    def autolight(self):
        logger.info("开始调节自动背光")
        device.swipe(0.5, 0.014, 0.5, 0.385)
        device.implicitly_wait(5)

        device.xpath('//*[@resource-id="com.android.systemui:id/auto_switch"]').click()
        logger.info("自动背光按钮已点击")
        device.press("home")

    def ScreenSettings(self):
        try:
            logger.info("开始设置屏保时间")
            device.app_start("com.android.settings")
            device.implicitly_wait(5)
            device(scrollable=True).scroll.to(text="显示")
            device(resourceId="android:id/title", text="显示").click()
            device.implicitly_wait(1)
            device.shell("input keyevent 20")   # 向下操作
            device.shell("input keyevent 20")
            device.shell("input keyevent 20")
            device.xpath('//*[@text="屏保"]').click()
            device.implicitly_wait(3)
            device.xpath('//*[@text="启用时机"]').click()
            device.implicitly_wait(3)
            device.xpath('//*[@text="5 分钟"]').click()
            logger.info("已设置屏保为5分钟")
        except Exception as e:
            logger.error(e)
            AssertMethod.assert_Fail(self)

    def setting_wifi_btn(self):
        try:
            logger.info("点击设置里所有相关按钮")
            device.app_start("com.android.settings")
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="网络和互联网").click()
            device.implicitly_wait(3)
            logger.info("开始连点——wifi开关按钮")
            device(resourceId="android:id/widget_frame").click_gone(maxretry=10, interval=0.1)
            device.implicitly_wait(3)
            device.xpath('//*[@text="WLAN"]').click()
            time.sleep(1)
            for i in range(30):
                device.shell("input keyevent --longpress 20")   # 重复向下操作
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="WLAN 偏好设置").click()
            logger.info("开始连点——自动开启WiFi按钮")
            device(resourceId="android:id/title", text="自动开启 WLAN").click()
            if device(resourceId="com.android.settings:id/alertTitle").exists:
                device.implicitly_wait(1)
                device.xpath('//*[@resource-id="android:id/button1"]').click()
                time.sleep(1)
            device(resourceId="android:id/title", text="自动开启 WLAN").click_gone(maxretry=10, interval=0.1)
            device.implicitly_wait(1)
            logger.info("开始连点——公共网络通知按钮")
            device(resourceId="android:id/title", text="附近有公共网络时发出通知").click_gone(maxretry=10, interval=0.1)
            time.sleep(1)
            device.shell('input keyevent --longpress 4')  # 返回到wifi设置初始进入界面
            time.sleep(1)
            device.xpath('//*[@text="热点和网络共享"]').click()
            device.implicitly_wait(3)
            device.xpath('//*[@text="WLAN 热点"]').click()
            device.implicitly_wait(3)
            logger.info("开始连点——wifi热点开关按钮")
            device(resourceId="com.android.settings:id/switch_text").click_gone(maxretry=10, interval=0.1)
            device.implicitly_wait(3)
            logger.info("开始连点——自动关闭热点开关按钮")
            device(resourceId="android:id/title", text="自动关闭热点").click_gone(maxretry=10, interval=0.1)
        except Exception as e:
            logger.error(e)
            AssertMethod.assert_Fail(self)

    def setting_bluetooth_btn(self):
        try:
            device.app_start("com.android.settings")
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="已连接的设备").click()
            device.implicitly_wait(3)
            device.xpath('//*[@text="连接偏好设置"]').click()
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="蓝牙").click()
            device.implicitly_wait(3)
            logger.info("开始连点——蓝牙开关按钮")
            device(resourceId="android:id/switch_widget").click_gone(maxretry=10, interval=0.1)
            time.sleep(1)

        except Exception as e:
            logger.error(e)
            AssertMethod.assert_Fail(self)

    def setting_app_btn(self):
        try:
            device.app_start("com.android.settings")
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="应用").click()
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="特殊应用权限").click()
            device.implicitly_wait(3)
            logger.info("进入----所有文件权限访问")
            device(resourceId="android:id/title", text="所有文件访问权限").click()
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="音乐").click()
            logger.info("开始连点——该应用文件权限开关按钮")
            device(resourceId="android:id/switch_widget").click_gone(maxretry=10, interval=0.1)
            time.sleep(1)
            device.shell('input keyevent --longpress 4')  # 返回

            device.implicitly_wait(3)
            logger.info("进入----显示其它应用上层")
            device(resourceId="android:id/title", text="显示在其他应用的上层").click()
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="音乐").click()
            logger.info("开始连点——音乐显示上层权限开关按钮")
            device.implicitly_wait(3)
            device(resourceId="android:id/switch_widget").click_gone(maxretry=10, interval=0.1)
            time.sleep(1)
            device.shell('input keyevent --longpress 4')  # 返回

            device.implicitly_wait(3)
            logger.info("进入----勿扰权限")
            device(resourceId="android:id/title", text="“勿扰”权限").click()
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="百度输入法").click()
            logger.info("开始连点——勿扰权限开关按钮")
            for i in range(5):
                device(resourceId="android:id/switch_widget").click()
                device.implicitly_wait(3)
                if device(resourceId="com.android.settings:id/title_template").exists:
                    device(resourceId="android:id/button1").click()
                    time.sleep(1)

            time.sleep(1)
            device.shell('input keyevent --longpress 4')  # 返回

            device.implicitly_wait(3)
            logger.info("进入----修改系统设置")
            device(resourceId="android:id/title", text="修改系统设置").click()
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="音乐").click()
            logger.info("开始连点——修改系统开关按钮")
            device.implicitly_wait(3)
            device(resourceId="android:id/switch_widget").click_gone(maxretry=10, interval=0.1)
            time.sleep(1)
            device.shell('input keyevent --longpress 4')  # 返回

        except Exception as e:

            logger.error(e)
            AssertMethod.assert_Fail(self)

    def setting_notice_btn(self):
        try:
            device.app_start("com.android.settings")
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="通知").click()
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="通知历史记录").click()
            logger.info("开始连点——通知历史记录开关按钮")
            device.implicitly_wait(3)
            device(resourceId="android:id/switch_widget").click_gone(maxretry=10, interval=0.1)
            time.sleep(1)
            device.shell('input keyevent 4')  # 返回

            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="对话泡").click()
            device.implicitly_wait(3)
            logger.info("开始连点——通知对话泡开关按钮")
            device(resourceId="android:id/switch_widget").click_gone(maxretry=10, interval=0.1)
            time.sleep(1)
            device.shell('input keyevent 4')  # 返回

            for i in range(10):
                device.shell("input keyevent 20")   # 重复向下操作
            device.implicitly_wait(3)
            logger.info("开始连点——隐藏状态栏通知开关按钮")
            device(resourceId="android:id/title", text="隐藏状态栏中的无声通知").click_gone(maxretry=10, interval=0.1)
            time.sleep(1)

            device.implicitly_wait(3)
            logger.info("开始连点——允许显示通知延后开关按钮")
            device(resourceId="android:id/title", text="允许显示通知延后选项").click_gone(maxretry=10, interval=0.1)
            time.sleep(1)

            device.implicitly_wait(3)
            logger.info("开始连点——应用图标上的通知圆点开关按钮")
            device(resourceId="android:id/title", text="应用图标上的通知圆点").click_gone(maxretry=10, interval=0.1)
            time.sleep(1)

        except Exception as e:
            logger.error(e)
            AssertMethod.assert_Fail(self)

    def setting_storage_btn(self):
        try:
            device.app_start("com.android.settings")
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="存储").click()
            logger.info("开始连点——存储管理开关按钮")
            for i in range(5):
                device.implicitly_wait(3)
                device(resourceId="android:id/widget_frame").click()
                if device(resourceId="android:id/message").exists:
                    time.sleep(1)
                    device(resourceId="android:id/button1").click()

        except Exception as e:
            logger.error(e)
            AssertMethod.assert_Fail(self)

    def setting_display_btn(self):
        try:
            device.app_start("com.android.settings")
            device(scrollable=True).scroll.to(text='关于本机')  # 滑动
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="显示").click()
            logger.info("开始连点——自动调节亮度开关按钮")
            for i in range(10):
                device.implicitly_wait(3)
                device.xpath('//*[@resource-id="com.android.settings:id/detail_content"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]').click()

            logger.info("开始连点——护眼模式开关按钮")
            for j in range(10):
                device.implicitly_wait(3)
                device.xpath('//*[@resource-id="com.android.settings:id/detail_content"]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView[1]/android.widget.LinearLayout[8]/android.widget.LinearLayout[2]').click()
            time.sleep(1)


            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="屏保").click()
            logger.info("开始连点——屏保开关按钮")
            device.implicitly_wait(3)
            device(resourceId="android:id/switch_widget").click_gone(maxretry=10, interval=0.1)

        except Exception as e:
            logger.error(e)
            AssertMethod.assert_Fail(self)

    def setting_secret_btn(self):
        try:
            device.app_start("com.android.settings")
            device(scrollable=True).scroll.to(text='关于平板电脑')  # 滑动
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="隐私").click()

            logger.info("开始连点——显示密码开关按钮")
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="显示密码").click_gone(maxretry=10, interval=0.1)

            logger.info("开始连点——剪切板通知开关按钮")
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="显示剪贴板访问通知").click_gone(maxretry=10, interval=0.1)

        except Exception as e:
            logger.error(e)
            AssertMethod.assert_Fail(self)

    def setting_system_btn(self):
        try:
            device.app_start("com.android.settings")
            device(scrollable=True).scroll.to(text='关于平板电脑')  # 滑动
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="系统").click()
            logger.info("进入语言和输入法界面")
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="语言和输入法").click()

            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="实体键盘").click()
            logger.info("开始连点——屏幕键盘开关按钮")
            device.implicitly_wait(3)
            device(resourceId="android:id/switch_widget").click_gone(maxretry=10, interval=0.1)
            time.sleep(1)
            device.shell('input keyevent 4')  # 返回

            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="拼写检查工具").click()
            logger.info("开始连点——拼写检查工具开关按钮")
            device.implicitly_wait(3)
            device(resourceId="android:id/switch_widget").click_gone(maxretry=10, interval=0.1)
            time.sleep(1)
            device.shell('input keyevent --longpress 4')  # 返回

            logger.info("进入日期和时间界面")
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="日期和时间").click()
            logger.info("开始连点——语言区域开关按钮")
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="使用默认语言区域").click_gone(maxretry=10, interval=0.1)

            logger.info("开始连点——24小时制开关按钮")
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="使用 24 小时制").click_gone(maxretry=10, interval=0.1)

        except Exception as e:
            logger.error(e)
            AssertMethod.assert_Fail(self)

    def setting_game_btn(self):
        try:
            device.app_start("com.android.settings")
            device(scrollable=True).scroll.to(text='关于平板电脑')  # 滑动
            logger.info("进入游戏模式界面")
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="游戏模式设置").click()
            logger.info("开始连点——游戏模式开关按钮")
            device.implicitly_wait(3)
            device(resourceId="android:id/switch_widget").click_gone(maxretry=10, interval=0.1)

            if device(resourceId="android:id/title", text="防打扰设置").exists(timeout=3):
                logger.info("游戏模式已开启")
                pass
            else:
                logger.info("游戏模式未开启，现在打开")
                device.implicitly_wait(3)
                device(resourceId="android:id/title", text="游戏模式").click()

            logger.info("进入防打扰设置界面")
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="防打扰设置").click()
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="⾳视频语⾳").click()

            logger.info("开始连点——屏蔽通话开关按钮")
            device.implicitly_wait(3)
            device(resourceId="android:id/switch_widget").click_gone(maxretry=10, interval=0.1)
            time.sleep(1)
            device.shell('input keyevent 4')  # 返回

            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="消息管理").click()
            logger.info("开始连点——屏蔽所有通知开关按钮")
            device.implicitly_wait(3)
            device(resourceId="android:id/switch_widget").click_gone(maxretry=10, interval=0.1)
            time.sleep(1)
            device.shell('input keyevent --longpress 4')  # 返回

            logger.info("进入GPU设置界面")
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="GPU设置").click()
            logger.info("开始连点——GPU标准模式开关按钮")
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="标准模式").click_gone(maxretry=10, interval=0.1)
            time.sleep(1)

            logger.info("开始连点——GPU自定义模式开关按钮")
            device.implicitly_wait(3)
            device(resourceId="android:id/title", text="⾃定义模式").click_gone(maxretry=10, interval=0.1)

        except Exception as e:
            logger.error(e)
            AssertMethod.assert_Fail(self)

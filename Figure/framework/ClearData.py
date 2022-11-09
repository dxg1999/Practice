# coding： utf-8

# @Author: Duanxiaogang
# @File :ClearData.py
# @DATE :2022/11/7
import time
from framework.logger import Loggoer   # 导入日志模块代码
from framework.get_devices import GetAdbDevice  # 导入设备获取类

logger = Loggoer(logger="Figure").getlogger()  # 获取Logger工厂类的方法
dut = GetAdbDevice()
device = dut.get_device()


class Clear_Data(object):
    def clearWB(self):
        time.sleep(2)
        device.app_start("com.android.settings")
        logger.info("清理wifi蓝牙测试环境")
        device(scrollable=True).scroll.to(text="系统")
        device(text="系统").click()
        device.implicitly_wait(3)
        device(resourceId="android:id/title", text="重置选项").click()
        device.implicitly_wait(3)
        device(resourceId="android:id/title", text="重置 WLAN、移动数据网络和蓝牙设置").click()
        device.implicitly_wait(3)
        device(resourceId="com.android.settings:id/initiate_reset_network").click()
        device.implicitly_wait(3)
        device(resourceId="com.android.settings:id/execute_reset_network").click()
        device.implicitly_wait(3)
        device.app_clear("com.android.settings")


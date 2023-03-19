# coding： utf-8

# @Author: Duanxiaogang
# @File :kill_app.py
# @DATE :2022/11/15
import time

from conf.logger import Logger
from common.get_devices import GetAdbDevice

logger = Logger(logger="log_msg").getlogger()
dut = GetAdbDevice()
device = dut.get_device()


class KillApp(object):
    def clearapp_test(self):
        device.shell("input keyevent 187")
        device.implicitly_wait(1)
        device.xpath('//*[@resource-id="com.android.launcher3:id/clear_all_iv"]').click()
        device.press("home")
        time.sleep(1)


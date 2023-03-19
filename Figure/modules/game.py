# coding： utf-8

# @Author: Duanxiaogang
# @File :game.py
# @DATE :2022/11/4
import time
from framework.logger import Loggoer
from framework.get_devices import GetAdbDevice
import unittest
from framework.fail import Failed
import random
import threading
import inspect
import ctypes
import aircv

logger = Loggoer(logger="Figure").getlogger()
dut = GetAdbDevice()
device = dut.get_device()
flag = 0


def tt_Equipment():
    while True:
        resource_list = [(1537, 777), (1647, 590), (1837, 483), (357, 400)]  # 技能加点坐标和装备购买坐标
        # 攻击坐标(2070, 846)
        select_re = random.choice(resource_list)
        device.click(select_re[0], select_re[1])
        time.sleep(1)


def tt_move():
    # 中心(352.24, 777) 上(352.24, 660) 下(352.24, 880) 左(214, 781.86) 右(476, 781.86)

    while True:
        device.touch.down(352.24, 777).move(556, 660).sleep(2).up(556, 660)
        direction_list = [(352, 660), (352, 880), (214, 772), (476, 772)]
        select_direction = random.choice(direction_list)
        device.touch.down(352.24, 777).move(select_direction[0], select_direction[1]).sleep(2).up(select_direction[0], select_direction[1])
        time.sleep(1)


def tt_skill():
    while True:
        skill_list = [(1637, 865), (1742, 693), (1937, 581)]
        select_skill = random.choice(skill_list)
        device.click(select_skill[0], select_skill[1])
        time.sleep(1)


def tt_attack():
    while True:
        device.click(2070, 846)
        time.sleep(1)


def stop_thread(thread, exctype=SystemExit):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(thread.ident)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def monitor_game():
    while True:
        time.sleep(10)
        global flag
        device.screenshot('../screenshots/test.png')
        test = aircv.imread('../screenshots/test.png')
        gameover = aircv.imread('../config/over.jpg')
        result = aircv.find_template(test, gameover)
        if result is None:
            flag = 0
            pass
        else:
            print('游戏结束')
            flag = 1


class Game(unittest.TestCase):

    def GameStart_test(self):
        logger.info("打开游戏应用")
        device.app_start("com.tencent.tmgp.sgame")
        time.sleep(21)

    def GameSelect_test(self):
        try:
            time.sleep(1)
            logger.info("关闭启动弹窗")
            device.click(1932, 140)
            time.sleep(1)
            logger.info("进入离线模式")
            device.click(2127, 274)
            time.sleep(1)
            logger.info("开始游戏")
            device.click(1813, 851)
            time.sleep(2)
            logger.info("开始随机选取对战英雄。。。")
            hero_list = [(261, 176), (438, 176), (261, 362), (438, 362), (261, 563), (438, 563), (261, 749), (438, 749)]
            select_hero1 = random.choice(hero_list)
            select_hero2 = random.choice(hero_list)
            device.click(select_hero1[0], select_hero1[1])
            time.sleep(1)
            logger.info("开始挑选对手")
            device.click(2070, 925)
            time.sleep(1)
            device.click(select_hero2[0], select_hero2[1])
            time.sleep(1)
            logger.info("开始对战")
            device.click(2070, 925)
            time.sleep(10)
        except Exception as e:
            error_info = logger.info(f"异常：{e}")
            Failed.failed_test(self, error_info)

    def GameRunning_test(self):
        logger.info("游戏内开始操作对战")
        time.sleep(6)
        device.touch.down(352.24, 777).move(556, 660).sleep(12).up(556, 660)
        p1 = threading.Thread(target=tt_move, name="demo1")
        p2 = threading.Thread(target=tt_Equipment, name="demo2")
        p3 = threading.Thread(target=tt_skill, name="demo3")
        p4 = threading.Thread(target=tt_attack, name="demo4")
        p5 = threading.Thread(target=monitor_game, name="demo5")
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        time.sleep(100)
        logger.info("进行游戏中power键灭屏")
        device.press("power")
        time.sleep(3)
        logger.info("点击power键亮屏")
        device.press("power")
        time.sleep(1)
        logger.info("继续游戏。。。")
        while True:
            time.sleep(1)
            global flag
            if flag == 1:
                logger.info("游戏已结束，停止线程方法")
                stop_thread(p1)
                stop_thread(p2)
                stop_thread(p3)
                stop_thread(p4)
                stop_thread(p5)
                break

    def GameClear_test(self):
        logger.info("清空游戏应用")
        device.app_clear("com.tencent.tmgp.sgame")

# coding： utf-8

# @Author: Duanxiaogang
# @File :logger.py
# @DATE :2022/11/18
import os
import logging
import time


class Logger(object):

    def __init__(self, logger):
        '''
        指定保存日志文件路径、级别
        '''
        # 创建一个logger对象进行初始化
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 获取文件路径和时间
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))

        log_path = os.path.dirname(os.path.abspath('.')) + '/AutoInterface/log/'
        log_name = log_path + rq + '.log'

        # 判断当前日志对象中是否有处理器，如果没有，则添加处理器——解决log重复打印
        if not self.logger.handlers:
            # 创建一个handler进行日志写入
            fileH = logging.FileHandler(log_name)
            fileH.setLevel(logging.DEBUG)

            # 创建一个handler用于控制台输出
            controlH = logging.StreamHandler()
            controlH.setLevel(logging.INFO)

            # 定义handler的输出格式
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
            fileH.setFormatter(formatter)
            controlH.setFormatter(formatter)

            # 添加handler
            self.logger.addHandler(fileH)
            self.logger.addHandler(controlH)

    def getlogger(self):
        return self.logger

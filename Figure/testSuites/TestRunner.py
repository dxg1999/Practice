# coding： utf-8

# @Author: Duanxiaogang
# @File :TestRunner.py
# @DATE :2022/10/27

import HTMLTestRunner
import os
import unittest
import time


def createsuite():

    # 将测试用例加入到测试容器（套件）中 pattern='test_*.py'
    discover = unittest.defaultTestLoader.discover('../testSuites',pattern='test_smoke.py',top_level_dir=None)
    return discover



if __name__ == '__main__':

    # suite = unittest.defaultTestLoader.discover('../testSuites',pattern='test_*.py',top_level_dir=None)
    report_path = os.path.dirname(os.path.abspath('.')) + '/testReport/'
    now = time.strftime("%y%m%d%H%M%S", time.localtime())
    HtmlFile = report_path + now + 'HtmlTest.html'

    with open(HtmlFile, 'w', encoding='utf-8') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='Test Report',
            description='自动化测试 generated by HTMLTestRunner.',
            verbosity=2
        )
        suite = createsuite()
        runner.run(suite)

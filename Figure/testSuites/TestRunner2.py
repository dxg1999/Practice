# coding： utf-8

# @Author: Duanxiaogang
# @File :TestRunner.py
# @DATE :2022/10/27

from BeautifulReport import BeautifulReport
import os
import unittest
import time
from framework.feishuapi import feishu
from framework.get_bh_result import get_test_result


def createsuite():

    # 将测试用例加入到测试容器（套件）中 pattern='test_*.py'
    discover = unittest.defaultTestLoader.discover('../testSuites', pattern='test_practice.py', top_level_dir=None)
    return discover


if __name__ == '__main__':

    # suite = unittest.defaultTestLoader.discover('../testSuites',pattern='test_*.py',top_level_dir=None)
    report_path = os.path.dirname(os.path.abspath('.')) + '\\testReport\\'
    now = time.strftime("%y%m%d%H%M%S", time.localtime())
    HtmlFile = now + 'HtmlTest.html'

    suite = createsuite()
    # 加载执行用例生成报告
    runner = BeautifulReport(suite)
    runner.report(description='Demo实例报告', report_dir=report_path, filename=HtmlFile)

    time.sleep(2)
    htmlfile = report_path + HtmlFile
    result = get_test_result(htmlfile)
    feishu.send_text_msg(result)

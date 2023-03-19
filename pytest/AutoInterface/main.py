# coding： utf-8

# @Author: Duanxiaogang
# @File :main.py
# @DATE :2022/11/18

import os
import time
from common.feishuapi import feishu
import pytest

if __name__ == '__main__':

    # 当前路径(使用 abspath 方法可通过dos窗口执行)
    current_path = os.path.dirname(os.path.abspath(__file__))
    # json报告路径
    json_report_path = os.path.join(current_path, 'report/json')
    # html报告路径
    html_report_path = os.path.join(current_path, 'report/HTML')

    # 执行pytest下的用例并生成json文件
    '''
        -q: 安静模式, 不输出环境信息
        -v: 丰富信息模式, 输出更详细的用例执行信息
        -s: 显示程序中的print/logging输出
    '''
    pytest.main(['-s', '-v', r'./TestCase/test_case.py', '--alluredir=%s' % json_report_path, '--clean-alluredir'])
    # 把json文件转成html报告
    os.system('allure generate "%s" -o "%s" --clean' % (json_report_path, html_report_path))
    # 程序运行之后，自动启动报告，如果不想启动报告，可注释这段代码
    os.system(f"allure serve ./report/json -h 127.0.0.1 -p 9999")
    # 发送消息进行通知
    feishu.send_text_msg("测试已完成，请查看报告")



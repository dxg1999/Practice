# coding： utf-8

# @Author: Duanxiaogang
# @File :get_bh_result.py
# @DATE :2023/1/5

from selenium import webdriver
import time
from selenium.webdriver.common.by import *


def get_test_result(htmlfile):
    '''
    获取测试报告网页中的结果数据
    :return:
    '''

    driver = webdriver.Chrome()
    driver.get(htmlfile)
    time.sleep(2)
    dataList = []

    total = float(driver.find_element(By.XPATH,'//*[@id="testAll"]').text)
    passed = float(driver.find_element(By.XPATH,'//*[@id="testPass"]').text)
    error = float(driver.find_element(By.XPATH,'//*[@id="testFail"]').text)
    passing_rate = (round(passed / total, 5)) * 100  # 保留5位小数
    start_time = driver.find_element(By.XPATH,'//*[@id="beginTime"]').text
    lists = [start_time, total, passed, error, passing_rate]
    dataList.append(lists)
    driver.quit()

    return dataList

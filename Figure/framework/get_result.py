# coding： utf-8

# @Author: Duanxiaogang
# @File :get_result.py
# @DATE :2022/11/30

from lxml import etree


def case_result(htmlfile):

    html_contain = etree.parse(htmlfile, etree.HTMLParser())

    #  定位xpath
    parse_data = html_contain.xpath('//tr[@id="total_row"]')
    start_time = html_contain.xpath('/html/body/div[1]/p[1]/text()')[0]
    dataList = []
    for data in parse_data:
        total = float(data.xpath('./td[2]/text()')[0])
        passed = float(data.xpath('./td[3]/text()')[0])
        error = total - passed
        passing_rate = (round(passed/total, 5))*100   # 保留5位小数
        lists = [start_time, total, passed, error, passing_rate]
        dataList.append(lists)

    return dataList




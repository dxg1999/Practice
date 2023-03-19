# coding： utf-8

# @Author: Duanxiaogang
# @File :dataprocess.py
# @DATE :2022/11/29

from common.ReadExcel import *
from logging import config, getLogger

from common.Assert import *
import json
from conf.logger import Logger

log = Logger(logger="log_msg").getlogger()


class Procee(object):

        def __init__(self):
            self.case = []
            self.red = ReadExcel()

        def runCase_excel_Data(self, CASE_PATH):

            case_key = ['用例编号', '用例名称', '请求URL', '请求方式','headers', '请求参数', '预期结果', '是否执行']

            for i in self.red.read_case_data(CASE_PATH):
                if i[7] == '是':
                    self.case.append(i)
                else:
                    continue
            log.info('用例执行状态查询完成')
            for i in self.case:
                data = dict(zip(case_key, list(i)))
                log.info(f'用例执行：{data}')
                print(data)
                yield data



        def case_result(self):
           re = AssertMethod()
           result = re.case_test_result()



if __name__ == '__main__':
    # data = {'extentSource': 'dolor', 'gateTime': '1965-07-07T04:42:24.172Z', 'gpsTime': '1999-12-19T06:31:27.724Z', 'id': 'in laborum nulla ex est', 'imei': '202139954700001', 'lat': 28.683908976, 'lng': 106.55359412, 'positionType': 'GPS'}

    # print(data)
    p = Procee()
    for i in p.runCase_excel_Data():
        print(type(i['headers']))
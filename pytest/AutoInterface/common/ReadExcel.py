# coding： utf-8

# @Author: Duanxiaogang
# @File :ReadExcel.py
# @DATE :2022/11/29

"""
读取Excel 数据
"""

from common import requestmethod
from conf import settings
import json

from conf import logger
from logging import config, getLogger
import xlrd
config.dictConfig(logger.LOGGING_DIC)
log = getLogger('log_msg')


class ReadExcel(object):

    def __init__(self, caseID=None, caseName=None, url=None, method=None, headers=None, caseParm=None, caseExpect=None, runStatus=None):
        self.caseID = caseID
        self.caseName = caseName
        self.url = url
        self.method = method
        self.headers = headers
        self.caseParm = caseParm
        self.caseExpect = caseExpect
        self.runStatus = runStatus

    def read_case_data(self, CASE_PATH):
       text  = xlrd.open_workbook(CASE_PATH)
       table = text.sheets()[0]
       i = 0
       caee_key = table.row_values(0)
       print(caee_key)

       try:
           log.info('************获取自动化用例**************')
           while True:

               i += 1
               row = table.row_values(i)
               self.caseID = int(row[0])
               self.caseName = row[1]
               self.url =  row[2]
               self.method = row[3]
               self.headers = row[4]
               self.caseParm = eval(row[5])
               self.caseExpect = row[6]
               self.runStatus = row[7]

               yield self.caseID, self.caseName, self.url, self.method,self.headers, self.caseParm, self.caseExpect, self.runStatus
       except Exception as ex:
           log.error(f'成功读取所有测试用例,成抛出异常信息list index out of range无影响 本次异常信息: {ex}')



if __name__ == '__main__':
    pass
    # red = ReadExcel()
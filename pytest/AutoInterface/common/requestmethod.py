# coding： utf-8

# @Author: Duanxiaogang
# @File :requestmethod.py
# @DATE :2022/11/18

import requests
from conf.logger import Logger

log = Logger(logger="log_msg").getlogger()


class RequestMethod(object):
    def post_requests(self, url, headers, data):
        """
        # 忽略不安全的请求警告信息
        # requests.packages.urllib3.disable_warnings()
        # 遇到requests的ssl验证，若想直接跳过不验证，设置verify=False即可
        """
        try:
            response = requests.post(url=url,headers=headers,data=data,verify=False)

            return response
        except Exception as e:
            print(e)

    def get_requests(self, url, headers, data=None):
        # 忽略不安全的请求警告信息
        # requests.packages.urllib3.disable_warnings()
        try:
            response = requests.get(url=url, headers=headers, data=data, verify=False)
            return response
        except Exception as e:
            print(e)

    def request(self, url, method, headers=None, data=None):
        # # 忽略不安全的请求警告信息
        # requests.packages.urllib3.disable_warnings()
        # requests.adapters.DEFAULT_RETRIES = 5

        if method == "POST":
            log.info('调用POST请求')
            response = self.post_requests(url, headers, data)
        elif method == "GET":
            log.info('调用GET请求')
            response = self.get_requests(url, headers, data)
        # 将响应的的数据以字典数据结构和json数据格式返回
        else:
            log.warning('请求方式不存在')

        return response



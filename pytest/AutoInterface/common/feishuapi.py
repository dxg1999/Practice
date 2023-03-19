# coding： utf-8

# @Author: Duanxiaogang
# @File :feishuapi.py
# @DATE :2022/11/29

import json
import requests
import urllib3


class feishu():
    # 飞书机器人wehook地址
    url = 'https://open.feishu.cn/open-apis/bot/v2/hook/1b5930de-5d83-4cc2-b31f-dc3fb5789885'
    headers = {
        'Content-Type': 'application/json',
    }

    @classmethod
    def send_text_msg(cls, text):
        msg = {
            "msg_type": "text",
            "content": {
                "text": text
            }
        }
        urllib3.disable_warnings()  # 等价于requests.packages.urllib3.disable_warnings()
        response = requests.request("POST", cls.url, headers=cls.headers, data=json.dumps(msg), verify=False)
        return response


if __name__ == '__main__':
    feishu.send_text_msg('{code:200,pass:90%}')
    pass


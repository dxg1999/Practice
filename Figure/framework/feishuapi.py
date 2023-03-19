# coding： utf-8

# @Author: Duanxiaogang
# @File :feishuapi.py
# @DATE :2022/11/29

import json
import requests
import urllib3


class feishu(object):
    # 飞书机器人wehook地址
    url = 'https://open.feishu.cn/open-apis/bot/v2/hook/b2d9fffa-4318-4fdd-b53e-a7336b48147e'
    # url = 'https://open.feishu.cn/open-apis/bot/v2/hook/1b5930de-5d83-4cc2-b31f-dc3fb5789885'

    headers = {
        'Content-Type': 'application/json',
        "charset": "utf-8",
    }

    @classmethod
    def send_text_msg(cls, data):
        msg = {
            "msg_type": "post",
            "content": {
                "post": {
                    "zh_cn": {
                        "title": "测试结果通知",
                        "content": [
                            [
                                {
                                    "tag": "text",
                                    "text": "项目有更新: "
                                },
                                {
                                    "tag": "a",
                                    "text": "请查看详情",
                                    "href": "https://www.baidu.com/"
                                }
                            ],
                            [
                                {
                                    "tag": "text",
                                    "text": "测试人员   :   "
                                },
                                {
                                    "tag": "text",
                                    "text": f"段小刚"
                                }
                             ],
                            [
                                {
                                    "tag": "text",
                                    "text": "成功率      : "
                                },
                                {
                                    "tag": "text",
                                    "text": f"{data[0][4]} %"
                                }
                            ],  # 成功率
                            [{
                                "tag": "text",
                                "text": "总用例数   : "
                            },
                                {
                                    "tag": "text",
                                    "text": f"{data[0][1]}"
                                }],  # 总用例数
                            [{
                                "tag": "text",
                                "text": "成功用例数: "
                            },
                                {
                                    "tag": "text",
                                    "text": f"{data[0][2]}"
                                }],  # 成功用例数

                            [{
                                "tag": "text",
                                "text": "失败用例数: "
                            },
                                {
                                    "tag": "text",
                                    "text": f"{data[0][3]}"
                                }],  # 失败用例数

                            [
                                {
                                    "tag": "text",
                                    "text": "执行时间   : "
                                },
                                {
                                    "tag": "text",
                                    "text": f"{data[0][0]}"
                                }
                            ],
                        ]
                    }
                }
            }
        }

        post_data = json.dumps(msg, ensure_ascii=True).encode("utf-8")
        # 取消警告

        urllib3.disable_warnings()   # 等价于requests.packages.urllib3.disable_warnings()
        response = requests.post(url=cls.url, headers=cls.headers, data=post_data, verify=False)
        return response



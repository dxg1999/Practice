# coding： utf-8

# @Author: Duanxiaogang
# @DATE :2022/11/29
import yaml
from conf import settings


class readYaml():
    def __init__(self):
        self.filename = settings.CASE_DATA_PATH

    def read_yaml(self):
        with open(self.filename, encoding='utf-8') as fs:
            # 避免报警告：yaml.FullLoader
            data = yaml.load(fs, Loader=yaml.FullLoader)
            return data

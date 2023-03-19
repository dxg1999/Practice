# coding： utf-8

# @Author: Duanxiaogang
# @File :Assert.py
# @DATE :2022/11/29


from conf.logger import Logger

log = Logger(logger="log_msg").getlogger()
"""
断言
"""


class AssertMethod(object):
    @classmethod
    def find_key(cls,json,key):
        """
                :参数 json: json  对象
                :参数 key: 字典key
                :return: 返回要查找的key
        """
        # isinstance判断一个对象的变量类型
        if isinstance(json, dict):
            for k, v in json.items():
                key_value = json.get(k)
                if k == key:
                    return {str(k): str(key_value)}
                elif isinstance(key_value, dict):
                    return cls.find_key(key_value, key)
                elif isinstance(key_value, list):
                    ret = cls.find_key(key_value, key)
                    if ret is not None:
                        return ret

        elif isinstance(json, list):
            for i in json:
                if i == key:
                    return i
                return cls.find_key(i, key)

    @classmethod
    def asert_one_key(cls, reponseResult, exceptReult):
        """
        :param reponseResult:  请求结果
        :param key: json  中的键值
        :param exceptReult: 预期结果
        :return:
        """
        excepts = eval(exceptReult)
        key = [i for i in excepts][0]
        Result = cls.find_key(reponseResult, key)

        if Result == excepts:
            log.info(f'测试通过PASS ====(实际结果:{Result},预期结果:{excepts})')
            assert Result == excepts
        else:
            log.warning(f'测试失败FIAL ====(实际结果:{Result},预期结果:{excepts}')
            assert False
        # assert Result == eval(exceptReult)

    @classmethod
    def asert_more_key(cls, reponseResult, exceptReult, keys):
        """
        :param reponseResult:  请求结果
        :param keys: json  可以传递多个键值code/userName/token
        :param exceptReult: 预期结果
        :return:
        """
        Result = {}
        excepts = eval(exceptReult)
        for i in keys.split('/'):
            v = cls.find_key(reponseResult, i)
            Result[i] = v.get(i)
        if Result == excepts:
            log.info(f'测试通过PASS ====(实际结果:{Result},预期结果:{excepts})')
            assert Result == excepts
        else:
            log.warning(f'测试失败Fial ====(实际结果:{Result},预期结果:{excepts}')
            assert False

    def assert_Fail(self):
        log.warning(f'测试失败 ====Fial')
        assert False


if __name__ == '__main__':
    pass
"""
======================
Time:2022/3/15 10:20
Author:feng
========================
"""
'''
ddt数据驱动测试
1.测试类前加@ddt
2.测试方法前加@list_data(测试函数）
3.在测试方法中定义一个参数，接收用例数据

给测试用例添加用例描述，需要再测试数据中添加title或desc字段，只针对字典数据类型
'''
import unittest
from unittestreport import ddt, list_data
from py_35unittest.login_func import login_check

cases = [
    {"title": "密码错误", "params": {"username": "dudu", "password": "123"}, "expected": {"code": 1, "msg": "账号或密码不正确"}},
    {"desc": "账号错误", "params": {"username": "dudu", "password": "1234"}, "expected": {"code": 1, "msg": "账号或密码不正确"}}
]


@ddt
class TestLogin2(unittest.TestCase):
    @list_data(cases)
    def test_login(self, item):
        # 准备测试用例
        expected = item["expected"]
        data = item["params"]
        # 调用被测函数，获取实际结果
        res = login_check(**data)
        # 断言
        self.assertEqual(res, expected)


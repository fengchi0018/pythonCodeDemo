"""
======================
Time:2022/3/15 13:24
Author:feng
========================
"""
'''
ddt的底层逻辑
1.存储测试数据
2.遍历测试数据，生成测试方法
'''
import unittest
from unittestreport import ddt, list_data

cases = [
    (1, 2, 3),
    (4, 5, 6)
]


@ddt
class TestDemo(unittest.TestCase):
    @list_data(cases)
    def test_01(self, item):
        print("item:", item)

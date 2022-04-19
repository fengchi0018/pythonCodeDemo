''''
@File  : test_audit.py
@Author: Feng
@Date  : 2022/4/16
@Desc  : 普通用户创建项目-管理员审核项目 流程测试
'''
import unittest
from unittestreport import ddt, list_data
import os

from demo.common.handle_path import DATA_DIR
from py_35_excel.excel_func import HandExcel


@ddt
class TestAudit(unittest.TestCase):
    excel = HandExcel(os.path.join(DATA_DIR), 'XX.xlsx')
    cases = excel.read_data()

    # 1.类方法前置【登录管理员，普通用户账号】
    @classmethod
    def setUpClass(cls) -> None:
        pass

    # 2.用例方法前置【普通用户创建项目】
    def setUp(self) -> None:
        pass

    # 3.用例执行：项目审核【审核前每次创建一个项目】
    @list_data(cases)
    def test_audit(self, item):
        pass

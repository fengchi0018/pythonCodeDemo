"""
======================
Time:2022/3/16 11:07
Author:feng
========================
"""
import os
import unittest
from unittestreport import ddt, list_data
from demo.common.handle_excel import HandExcel
from demo.login_func import login_check
from demo.common.handle_log import my_log
from demo.common.handle_path import DATA_DIR


@ddt
class TestLogin(unittest.TestCase):
    excel = HandExcel(os.path.join(DATA_DIR,"测试用例.xlsx"), "Sheet1")
    cases = excel.read_data()

    @list_data(cases)
    def test_login(self, item):
        expected = eval(item["expected"])
        param = eval(item["data"])
        # username = param["username"]
        # password = param["password"]
        # result = login_check(username, password)
        # 以上三行可用以下一行代替
        print(param)
        result = login_check(**param)
        # 获取行号
        row = item["case_id"] + 1
        try:
            self.assertEqual(expected, result)
        except AssertionError as e:
            self.excel.write_data(row=row, column=8, value="未通过")
            self.excel.write_data(row=row, column=9, value=str(result))
            my_log.error("用例--【{}】----执行失败".format(item['title']))
            # my_log.error(e)
            # 记录详细日志信息
            my_log.exception(e)
            # 为了让unittest识别这条是未通过的用例，需要将捕获的异常抛出去
            raise e
        else:
            self.excel.write_data(row=row, column=8, value="通过")
            my_log.info("用例--【{}】----执行成功".format(item['title']))



class TestLogin2(unittest.TestCase):
    pass

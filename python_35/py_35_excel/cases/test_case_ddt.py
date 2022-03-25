"""
======================
Time:2022/3/16 11:07
Author:feng
========================
"""
import unittest
from unittestreport import ddt, list_data
from py_35_excel.excel_func import HandExcel
from py_35_excel.login_func import login_check


@ddt
class TestLogin(unittest.TestCase):
    book = HandExcel(r"D:\PycharmProjects\python_35\py_35_excel\测试用例.xlsx", "Sheet1")
    data = book.read_data()

    @list_data(data)
    def test_login(self, item):
        expected = eval(item["expected"])
        param = eval(item["data"])
        # username = param["username"]
        # password = param["password"]
        # result = login_check(username, password)
        # 以上三行可用以下一行代替
        result = login_check(**param)
        # 获取行号
        row = item["case_id"] + 1
        try:
            self.assertEqual(expected, result)
        except AssertionError as e:
            print("测试未通过")
            self.book.write_data(row=row, column=8, value="未通过")
            self.book.write_data(row=row, column=9, value=str(result))
            # 为了让unittest识别这条是未通过的用例，需要将捕获的异常抛出去
            raise e
        else:
            print("测试通过")
            self.book.write_data(row=row, column=8, value="通过")


class TestLogin2(unittest.TestCase):
    pass

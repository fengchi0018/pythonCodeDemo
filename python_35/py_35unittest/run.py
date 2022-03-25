"""
======================
Time:2022/3/14 17:12
Author:feng
========================
"""
import unittest
from unittestreport import TestRunner

# # 创建测试套件，加载测试用例
# # 1.创建测试套件
# suit =unittest.TestSuite()
# # 2.创建测试用例加载器
# load =unittest.TestLoader()
# # 3加载测试用例到套件
# suit.addTest(load.discover(r'D:\PycharmProjects\python_35\py_35unittest\testcase'))
# # 以上三行可用以下一行代替
# # suit =unittest.defaultTestLoader.discover(r'D:\PycharmProjects\python_35\py_35unittest\testcase')
# # 创建测试用例程序
# runner = unittest.TextTestRunner()
# # 运行测试用例
# runner.run(suit)

suit = unittest.defaultTestLoader.discover(r"D:\PycharmProjects\python_35\py_35unittest\testcase")
runner = TestRunner(suit, title="测试报告", filename="report", templates=1, tester="测测")
runner.run()

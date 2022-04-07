"""
@Time    : 2022/4/6 20:18
@Author  : feng
"""
import unittest
from unittestreport import TestRunner
suit = unittest.defaultTestLoader.discover(r"D:\PycharmProjects\Python_C\python_35\demo\testcases")
runner = TestRunner(suit, title="测试报告", filename=r"D:\PycharmProjects\Python_C\python_35\demo\reports\report", templates=1, tester="测测")
runner.run()
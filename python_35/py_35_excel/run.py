"""
======================
Time:2022/3/16 12:01
Author:feng
========================
"""
from unittestreport import TestRunner
import unittest

suit = unittest.defaultTestLoader.discover(r"D:\PycharmProjects\python_35\py_35_excel\cases")
runner = TestRunner(suit)
runner.run()
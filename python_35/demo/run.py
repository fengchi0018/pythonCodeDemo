"""
@Time    : 2022/4/6 20:18
@Author  : feng
"""
import unittest
from unittestreport import TestRunner
from demo.common.handle_path import CASES_DIR,REPORT_DIR
import os
suit = unittest.defaultTestLoader.discover(CASES_DIR)
runner = TestRunner(suit, title="测试报告", filename=os.path.join(REPORT_DIR,"my_report"), templates=1, tester="测测")
runner.run()
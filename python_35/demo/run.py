"""
@Time    : 2022/4/6 20:18
@Author  : feng
右移：tab
左移：shift+ tab
"""
import unittest
from unittestreport import TestRunner
from demo.common.handle_path import CASES_DIR, REPORT_DIR
import os


def main():
    suit = unittest.defaultTestLoader.discover(CASES_DIR)
    runner = TestRunner(suit, title="测试报告", filename=os.path.join(REPORT_DIR, "my_report"), templates=1, tester="测测")
    runner.run()
    """
     1.失败后重新运行
        count：用来指定用例失败重运行的次数
        interval：指定每次重运行的时间间隔
    runner.run(count=3, interval=2)
    """
    """
     2、设置5个线程去执行用例
     runner.run(thread_count=5)
    """
    # 发送测试报告至邮箱
    runner.send_email(host='smtp.qq.com', port=465, user='fengchi0609@qq.com', password='tftzxhlsnwjwdhgf',
                      to_addrs=['2410639660@qq.com'], is_file=True)


if __name__ == '__main__':
    main()

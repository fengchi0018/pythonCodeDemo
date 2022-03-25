"""
======================
Time:2022/3/15 10:52
Author:feng
========================
"""


class Test:
    def __init__(self,name):
        print("1.初始化方法",name)

    def test(self):
        print("2.类方法")


if __name__ == '__main__':
    res = Test(22)
    res.test()

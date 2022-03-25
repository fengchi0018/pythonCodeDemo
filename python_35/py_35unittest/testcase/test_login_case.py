"""
======================
Time:2022/3/14 15:07
Author:feng
========================
"""
"""
unittest编写测试用例规范：
1.定义一个测试用例类，必须继承unittest 模块中的TestCase
2.测试用例中，一个test开头的方法就是一条测试用例
3.将测试用例执行中的代码逻辑写到对应的测试方法中(实例方法）
 #第一步：准备用例数据
 #第二部：调用被测的功能函数（发送请求调用接口），获取实际结果
 #第三步“断言


"""

import unittest
from py_35unittest.login_func import login_check


class TestLogin(unittest.TestCase):
    # 账号密码正常
    def test_login_pass(self):
        res = login_check("dudu", "123")
        expected = {"code": 0, "msg": "登录成功"}
        assert res == expected

    # 密码错误
    def test_login_pass_err(self):
        # 1.准备测试数据
        params = {"username": "dudu", "password": "1234"}
        expected = {"code": 1, "msg": "账号或密码不正确"}
        # 2.调用被测的功能函数，获取实际结果
        # result = login_check(username=params["username"],password=params["password"])
        result = login_check(**params)
        #3. 断言
        assert result == expected
class EstRegin(unittest.TestCase):
    def test_test(self):
        """测试描述"""
        assert "ok" == "ok"
if __name__ == '__main__':
    pass

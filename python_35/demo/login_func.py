"""
@Time    : 2022/4/6 20:18
@Author  : feng
"""
def login_check(username=None, password=None):
    if username != '' and password != '':
        if username == "dudu" and password == "123":
            return {"code": 0, "msg": "登录成功"}
        else:
            return {"code": 1, "msg": "账号或密码不正确"}
    else:
        return {"code": 1, "msg": "账号或密码不能为空"}


if __name__ == "__main__":
    res = login_check('', '')
    expected = {"code": 0, "msg": "登录成功"}
    print(res)
    assert res == expected
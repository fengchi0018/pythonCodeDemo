"""
======================
Time:2022/2/23 11:07
Author:feng
========================
"""
"""
assert:断言，成立无反应，不成立报错AssertError
AssertError:这个错误类型用来表示用例执行是否通过
"""
#预期结果
excepted = '注册成功'
# 实际结果
res="注册成功"
assert excepted == res

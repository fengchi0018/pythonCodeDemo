"""
======================
Time:2022/2/23 11:16
Author:feng
========================
"""
import keyword
'''
raise:主动抛出异常

'''



def add(a, b):
    if not isinstance(a, int):
        raise ValueError("a只能是int类型")
    if not isinstance(b, int):
        raise ValueError("b只能是int类型")
    return a + b


res = add('cc', 55)
print(res)

print(keyword.kwlist)

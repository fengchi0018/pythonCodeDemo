"""
======================
Time:2022/2/14 15:28
Author:feng
========================
"""
'''
内置函数:eval:取消字符串的""
'''
# 列表,元组转字符串
li =[1,2,3]
s =str(li)
tu =(1, 2, 3)
s1 =str(tu)
print(s,type(s))
print(s1,type(s1))

# 字符串转列表,元组
s ='[1, 2, 3]'
s2 ='(1, 2, 3)'
li2 =eval(s)
print(li2,type(li2))
tu1 =eval(s2)
print(tu,type(tu1))

ss ='12233'
list = list(ss)
print(list,type(list))
tuple =tuple(ss)
print(tuple,type(tuple))


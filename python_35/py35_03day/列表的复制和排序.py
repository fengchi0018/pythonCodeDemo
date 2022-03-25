"""
======================
Time:2022/2/14 14:58
Author:feng
========================
"""
'''
复制：copy
数字元素排序： sort()默认从大到小    sort(reverse =True)
列表倒叙：
        reverse()
        切片[：：-1]
'''
li =[1,2]
li2 =li.copy()
print(li)
print(li2)
li3 =[1,5,2,8,9,3]
li3.sort()
print(li3)
li3.sort(reverse=True)
print(li3)
li3.reverse()
print(li3)
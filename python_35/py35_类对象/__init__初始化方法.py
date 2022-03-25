"""
======================
Time:2022/3/7 15:45
Author:feng
========================
"""

# class Person:
#     pass
#
# musen =Person()
# musen.name = '木森'
# musen.age = 18

# -----------------init-------------
# 魔术方法：双下滑先开头和双下滑线结尾的方法
"""
__init__:初始化方法，在通过类创建对象的时候自动调用

"""


class Person:
    def __init__(self, name):
        """创建对象时，给对象设置对象属性"""
        self.name = name
        print("__init__")
    def funcz(self):
        self.height = 170


musen = Person("Musen")   #自动调用__init__方法
print(musen.name)
musen.funcz()
print(musen.height)

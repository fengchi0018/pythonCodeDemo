"""
======================
Time:2022/3/7 17:00
Author:feng
========================
"""
"""
 继承父类的所有属性和方法（私有的除外，_ _开头的书香和方法）
调用父类：类名.方法名（self,name)
          super().方法名(name)
          
多继承:可同时继承多个父类        
"""


class Demo(object):
    pass


class Demo2(Demo):
    pass


class Demo3:
    pass


class Demo4:
    pass

# 多继承
class Demo5(Demo3, Demo4):
    pass

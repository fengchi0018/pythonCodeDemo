"""
======================
Time:2022/3/7 16:45
Author:feng
========================
"""
"""
实例方法：只能通过对象调用。第一个参数self代表对象本身
           场景：方法内部要使用【对象的属性或者方法】，就要定义成对象方法
类方法：第一个参数cls：代表类本身
         可以通过类调用，也可以通过对象调用
         要先使用@classmethod声明
         场景：方法内部：要使用【类属性或者类方法】（不需要使用对象属性和方法）
静态方法：要先使用@staticmethod声明
           可以通过类调用，也可以通过对象调用
            场景：方法内部：既不使用【类属性或者类方法】也【不使用对象属性和方法】
"""
class Myclass:
    def func(self):
        print("实例方法")
    @classmethod
    def func_cls(cls):
        print("类方法")
    @staticmethod
    def func_static():
        print("静态方法")

my = Myclass()
my.func()

my.func_cls()
Myclass.func_cls()

my.func_static()
Myclass.func_static()


"""
======================
Time:2022/3/7 14:39
Author:feng
========================
"""
"""
 类：大驼峰格式
 通过类实例化对象：对象 = 类名()
 类属性：这类事务都具备这个属性，并且属性值一样的
         1.直接定义在类里面的变量
         2.类名.属性名 = 属性值
对象（实例）属性: 对象自己的特性
                   对象.属性名 = 属性值
 方法：定义在类里面的函数
       方法中的参数除了self之外，其他参数与函数是一致的
        不能用类直接调用，通过对象直接调用
"""


class Cat:
     leg =4
     eye =2
     def func(self,addr):
         print("抓老鼠")
         print("{}在{}抓老鼠".format(self.name,addr))
     pass


class Person(object):
    pass


# 通过猫类创建对象
coffee = Cat()
coffee.name ="加菲猫"
coffee.age =15
# 通过对象调用方法
coffee.func('在树上')
dingdang = Cat()

print(coffee)
print(dingdang)

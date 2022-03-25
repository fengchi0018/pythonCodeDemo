"""
======================
Time:2022/3/8 17:18
Author:feng
========================
"""
"""
动态属性设置：setattr()
             参数1：对象（类）
             参数2：属性名
             参数3：属性值
动态属性获取：getattr()
              参数1：对象（类）
              参数2：属性名
              参数3：非必传，设置一个属性不存在时返回的默认值，不传属性不存在时则报错
动态属性删除：delattr()
              参数1:对象(类)
              参数2:属性名
判断属性是否存在: hasattr()
                参数1:对象(类)
                参数2:属性名

"""

# --------------------------动态设置属性--------------
# class MyClass:
#     attr = 100


# 把字典中的键值对设置为类的属性和属性值
# data ={"name":"musen","age":18}
# for k,v in data.items():
#     setattr(MyClass,k,v)
# print(MyClass.__dict__)

# 把字典中的键值对设置为对象的属性和属性值
# m = MyClass()
# data ={"name":"musen","age":18}
# for k,v in data.items():
#     setattr(m,k,v)
# print(m.__dict__)
# print(m.name)
# print(m.age)
# --------------------------动态获取属性------------------
# class MyClass:
#     attr = 100
#     name = "木森"
#     age = 18
#
#
# key = input("请输入获取的属性")
# res = getattr(MyClass, key, None)
# print(res)
# -------------------动态删除属性----------------------------
# class MyClass:
#     attr = 100
#     name = "木森"
#     age = 18
# # 关键字：del   用来删除数据的关键字///元组不可变则不能删
# name = "aaaaaaaaa"
# li = [1,2,3]
# dic ={'a':1,"b":2}
# # del name
# del li[2]
# del dic['b']
# print(name)
# print(li)
# print(dic)
#
# key =input("请输入删除的属性")
# delattr(MyClass,key)
# print(MyClass.__dict__)
# -------------------动态判断属性是否存在----------------------------
class MyClass:
    attr = 100
    name = "木森"
    age = 18
if hasattr(MyClass,'name'):
     print(MyClass.name)
else:
    print("无该属性")

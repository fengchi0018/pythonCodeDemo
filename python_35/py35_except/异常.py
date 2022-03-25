"""
======================
Time:2022/2/23 10:44
Author:feng
========================
"""


try:
    print("可能错误的代码")
except Exception as e:
    print(e)   #打印错误
else:
    pass    # try中执行没有错时执行
finally:
   pass  # 不管try中代码执行是否出错，都会执行




# try:
#     print("可能错误的代码")
# except 异常类型 as e:
#     print(e)   #打印错误
# except 异常类型 as e:
#     print(e)  # 打印错误
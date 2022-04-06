"""
======================
Time:2022/2/22 16:28
Author:feng
========================
"""
"""
with as :上下管理器协议的启动器

with open 去操作文件会自动关闭文件

"""
with open(file='log.jpg', mode='rb') as f:
    res = f.read()
    print(res)


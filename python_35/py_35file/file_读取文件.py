"""
======================
Time:2022/2/22 15:42
Author:feng
========================
"""
"""
相对路径：
   .  :当前目录
   .. :上级目录
绝对路径:
   路径中包含专题字符的时候，要做特殊处理，字符串前加r或双斜杠
f = open(file=r'D:/desk/t更新.txt',mode='r',encoding='utf-8')
f = open(file='D:/desk//更新.txt',mode='r',encoding='utf-8')
"""
"""
内置参数open：
    参数file:文件名，路径
    参数mode:文件打开模式
        r:只读，文件不存在时报错
    参数encoding:指定编码格式
操作文件：
1.打开文件 open方法
2.进行操作：
    read()读取所有
    readline()读取一行
    readLines()按行读取文件，返回列表类型
    
3.关闭文件：close方法  
"""
f = open(file='D:/desk/更新.txt', mode='r', encoding='utf-8')
# f = open(file='更新.txt',mode='r',encoding='utf-8')
res = f.read()
print(res)
f.close()

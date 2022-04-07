''''
@File  : 操作配置文件.py
@Author: Feng
@Date  : 2022/4/7
@Desc  : 
'''
from configparser import ConfigParser

# 第一步：创建一个配置文件解析器对象
cp = ConfigParser()
# 第二步：读取配置文件中的内容到配置文件解析器中
cp.read('musen.ini',encoding='utf-8')
# 第三步：读取配置内容logging【配置块】下的filename【配置项】，get读取出来为string
res = cp.get('logging', 'filename')
# 读取数值字符
# num =cp.getint()
# 读取布尔类型
# boolean = cp.getboolean()
print(res)

# 写入配置文件
cp.set("mysql", "host", "10241.125.128")
with open('musen.ini', 'w', encoding='utf-8') as f:
    cp.write(fp=f)

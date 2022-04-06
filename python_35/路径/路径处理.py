''''
@File  : 路径处理.py
@Author: Feng
@Date  : 2022/4/2
@Desc  : 
'''
import os
''' 魔法变量
__name__          启动文件中__main__  非启动文件打印模块名
__file__          当前文件的文件名（pycharm中绝对路径）
'''
# 获取绝对路径
# p2 = os.path.abspath('test.txt')
# 获取父路径【不准确】
# p2 = os.path.abspath('..')
# # 获取当前路径绝对路径【常用】
# p2 = os.path.abspath(__file__)
# # 获取所在路径的目录
# pp2 =os.path.dirname(p2)
# 在当前文件中获取项目的根目录
# res =os.path.abspath(__file__)
# path1 =os.path.dirname(res)
# base_path = os.path.dirname(path1)
# print(path1)
# print(base_path)
# n = __name__
# f = __file__
# print(n)
# print(f)
# 获取项目根目录
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_path)
res = os.path.join(base_path,'py_35file')
print(res)

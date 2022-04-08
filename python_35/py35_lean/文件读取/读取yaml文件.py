''''
@File  : 读取yaml文件.py
@Author: Feng
@Date  : 2022/4/7
@Desc  : 读取出为字典或者列表
'''
import  yaml
with open('demo.yaml', 'r', encoding='utf-8') as f:
    res =yaml.load(f,Loader=yaml.Loader)

print(res)

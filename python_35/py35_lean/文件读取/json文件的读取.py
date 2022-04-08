''''
@File  : json文件的读取.py
@Author: Feng
@Date  : 2022/4/7
@Desc  : 
'''
import json

"""
python中:None   json:null
True                  true
False                 false

load:读取json文件转python数据
loads:json字符串转化为python数据
dumps: python数据转化为json字符串
"""
with open("data.json", "r", encoding='utf-8') as f:
    # 读取文件中的json数据并自动转化为py相关的数据类型
    res = json.load(f)
    # python转化为json
    # json.dump(f)

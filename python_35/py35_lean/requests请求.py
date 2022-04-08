''''
@File  : requests请求.py
@Author: Feng
@Date  : 2022/4/8
@Desc  : 
'''
import requests

url = ''
# -----表单
requests.post(url=url, data='')
# -------application/json
requests.post(url=url, json='')
# get查询字符串参数
# 1.接口地址后面用？拼接参数，参数=参数值
# 2.使用params
requests.get(url=url, params='')
# --------content-type:form-data----
# 文件上传
requests.post(url=url,files='')

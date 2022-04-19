''''
@File  : tool.py
@Author: Feng
@Date  : 2022/4/14
@Desc  : 
'''
import re
from demo.common.handle_conf import conf


# class TestData:
#     name = '123'
#     age = '18'
#
# # 动态属性修改
# s = "{'name':'#name#','age':'#age#','tel':'#tel#'}"

# 先在类属性中查找，再去配置文件中查找,类属性中和配置文件中的属性名与需要替换的位置数据保持一致 #tel#  tel
def replace(data, cls):
    """
    :param data: 替换的数据
    :param cls: 类方法
    :return:
    """
    while re.search('#(.+?)#', data):
        res = re.search('#(.+?)#', data)
        # print("被替换的内容：", res.group())  # #name#
        # print("替换的属性名：", res.group(1))  # name
        try:
            value = getattr(cls, res.group(1))  # 123
        except AttributeError:
            value = conf.get('testDate', res.group(1))
        # print("获取出的类属性值：", value)
        data = data.replace(res.group(), str(value))
    return data


# if __name__ == '__main__':
#     print(replace(s, TestData))

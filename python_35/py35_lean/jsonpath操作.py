''''
@File  : jsonpath操作.py
@Author: Feng
@Date  : 2022/4/8
@Desc  : 
'''
"""
jsonpath方法：
两个参数：数据，jsonpath表达式
语法：
$:根节点
.选取直接子节点
..获取子孙节点，不考虑层级
[]选择子节点/索引
[,]选择多个字段
@代表当前选中的节点（和条件过滤一起用）
[?(过滤条件）]

注意：无匹配数据返回False
"""
# import jsonpath
from jsonpath import jsonpath
data = {'code': 1,
        'count': 853,
        'data': [{'browseTotal': 0,
                  'collectionTotal': 0,
                  'commentTotal': 0,
                  'createDate': 1648547732000,
                  'examineStatus': 4,
                  'isClass': 0,
                  'likeTotal': 9,
                  'nickname': '测试2',
                  'opusId': 1241,
                  'opusType': 2,
                  'resource': 'https://dev-opus-1301823233.file.myqcloud.com/2022/03/12/29_Lec5Jua/16485477317620',
                  'status': 0,
                  'topics': ['一二三一二三一二三一二三一二三'],
                  'userId': 12},
                 {'browseTotal': 0,
                  'collectionTotal': 0,
                  'commentTotal': 2,
                  'createDate': 1648536873000,
                  'examineStatus': 4,
                  'isClass': 1,
                  'likeTotal': 15,
                  'nickname': '测试01测试01测试',
                  'opusId': 1240,
                  'opusType': 2,
                  'resource': 'https://dev-opus-1301823233.file.myqcloud.com/2022/03/6/29_CbLzSRE/616485368729140.webp',
                  'status': 0,
                  'topics': ['一二三一二三一二三一二三一二三'],
                  'userId': 6},
                 {'browseTotal': 0,
                  'collectionTotal': 0,
                  'commentTotal': 0,
                  'createDate': 1648536825000,
                  'examineStatus': 3,
                  'isClass': 0,
                  'likeTotal': 6,
                  'nickname': '测试2',
                  'opusId': 1239,
                  'opusType': 2,
                  'resource': 'http://dev-opus-1301823233.cos.ap-chengdu.myqcloud.com/2022/03/12/29_xf8LTXL/16485368252050?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDxtJ4bu8oX4HsfCeaXMxSpztaKznfvxOy%26q-sign-time%3D1649407653%3B1649411253%26q-key-time%3D1649407653%3B1649411253%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D243b3aaa032511981a09e5f261885a2715b99d30',
                  'status': 0,
                  'title': '给哈哈',
                  'topics': ['一二三一二三一二三一二三一二三'],
                  'userId': 12,
                  'violationContent': '1',
                  'violationType': 0},
                 {'browseTotal': 0,
                  'collectionTotal': 0,
                  'commentTotal': 1,
                  'createDate': 1648535320000,
                  'examineStatus': 4,
                  'isClass': 0,
                  'likeTotal': 10,
                  'nickname': '测试4',
                  'opusId': 1238,
                  'opusType': 2,
                  'resource': 'https://dev-opus-1301823233.file.myqcloud.com/2022/03/35/29_4t8Q3B4/3516485353201890.webp',
                  'status': 0,
                  'userId': 35},
                 {'browseTotal': 0,
                  'collectionTotal': 0,
                  'commentTotal': 0,
                  'createDate': 1648447827000,
                  'examineStatus': 4,
                  'isClass': 0,
                  'likeTotal': 17,
                  'nickname': '嘉文',
                  'opusId': 1237,
                  'opusType': 2,
                  'resource': 'https://dev-opus-1301823233.file.myqcloud.com/2022/03/10/28_BwfdSC8/16484478265570',
                  'status': 0,
                  'userId': 10},
                 ],
        'successful': True}
# 获取子节点字段
print(jsonpath(data,'$.code'))
print(jsonpath(data, '$[code]'))
# 获取多个字段
print(jsonpath(data,'$.data[1][nickname,opusId]'))
# 获取子孙节点
print(jsonpath(data,'$..createDate'))
# 获取索引数据
print(jsonpath(data,'$.data[1]'))
print(jsonpath(data,'$.data[1].createDate'))
# 筛选
print(jsonpath(data,'$.data[?(@.userId==13)]'))

print(jsonpath(data,'$.data[?(@.opusId==1241)].nickname'))
print(jsonpath(data,'$..[?(@.opusId==1241)].nickname'))


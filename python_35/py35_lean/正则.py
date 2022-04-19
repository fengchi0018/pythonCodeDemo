''''
@File  : 正则.py
@Author: Feng
@Date  : 2022/4/14
@Desc  :
\d   表示一个数字匹配
\D   非数字匹配
\s   空白字符
\S   非空白字符
\w   单词字符：字母数字，下划线
\W  非单词字符：除字母数字，下划线
.  任意字符，匹配所有
[]  枚举 例举匹配的字符
{num} 表示前一个字符出现num次
{num,} 表示前一个字符出现num次及以上
{n,m}  表示前一个字符出现num次至m次,贪婪模式，先匹配m次的
?非贪婪模式 关闭贪婪，0次或一次
+  表示一次以上 =={1,}
*   表示0次以上
^  匹配开头
$  匹配结尾
\b 表示单词边界 需使用转义符 r'\b str'
()分组
findall 匹配返回所有符合规则的数据，以列表形式返回
search:匹配并返回第一个符合规则的数据
'''
import re

s = '1234455hhL11hh5hkAK,一?1235'
res0 = re.findall('12', s)
res = re.findall('[125]', s)
res2 = re.findall('[0-9a-zA-Z]', s)
# 匹配中文
res3 = re.findall('[\u4e00-\u9fa5]', s)
res4 = re.findall('\d{3}', s)
res5 = re.findall('\d{3,}', s)
res6 = re.findall('\d{2,4}', s)
# 非贪婪模式，匹配2个
res7 = re.findall('\d{2,4}?', s)
print('res0:', res0)
print(res)
print(res2)
print(res3)
print(res4)
print(res5)
print(res6)
print(res7)
s1 = "{'id': '#123#', 'name': 'yy', 'age': '#18#', 'pp': '#jk#'}"
res8 = re.findall('#.{1,}#', s1)
res9 = re.findall('#.{1,}?#', s1)
res10 = re.findall('#.+?#', s1)
res11 = re.findall('#(.+?)#', s1)
print('res8:', res8)
print('res9:', res9)
print('res10:', res10)
print('res11:', res11)


# -----------------------------------------
class TestData:
    name = '123'
    age ='18'

# 动态属性修改
s= "{'name':'#name#','age':'#age#'}"
while re.search('#(.+?)#', s):
    res = re.search('#(.+?)#', s)
    print("被替换的内容：", res.group())  # #name#
    print("替换的属性名：", res.group(1))  # name
    value = getattr(TestData, res.group(1))  # 123
    print("获取出的类属性值：", value)
    s = s.replace(res.group(), str(value))
print(s)



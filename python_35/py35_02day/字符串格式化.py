"""
======================
Time:2022/2/11 17:02
Author:feng
========================
"""
"""
1.字符串拼接：+
2.format
3.%d  %s %f
4.字符串的f  表达式
"""

print("1.=================")
name =input("请输入名字：")
age = input("请输入年龄：")
print(name,"的年龄是",age)
line =name +"的年龄是"+age +"岁"
print(line)


print("2.重要=================")
line2 = "{}的年龄是{}岁"
print(line2.format(name,age))

# line2 ="{}的年龄是{}岁".format(name,age)
# print(line2)



print("3.=================")
line3 = "%s的年龄是%s岁"%("name",age)
print(line3)
print("4.=================")
line4 = f"{name}的年龄是{age}岁"
print(line4)

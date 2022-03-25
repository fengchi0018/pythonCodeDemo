"""
======================
Time:2022/2/14 13:49
Author:feng
========================
"""
"""
列表：使用[]表示，每个元素使用逗号隔开
列表是有序的，可切片,支持索引取值
可存放任意数据类型
list =[11,11.20,True,'11111',[1,"22]]
"""
info = [18,"木森",'男',"python"]
# 索引取值
res1 = info[0]
print(res1)
# 切片:"木森",'男'
res2 = info[1:3]
print(res2)
"""
列表的增删查改
添加数据： 
    append:列表结尾处添加一个元素
    insert:指定索引处添加元素
    extend:一次性在列表尾部添加多个元素
删除数据：
    remove:指定元素删除【存在多个只删除第一个】
    pop :指定索引删除【默认删除最后一个】调用会返回删除的数据
    clear:清空
修改数据
查找
    索引取值 list[索引值]
    查找元素对应的索引 list.index(”元素“)[元素不存在会报错]
    查找个数：list.count("2")
      
"""
list =[1,2,3]
list.append(4)
print(list)
list.append(5)
print(list)

# insert
list2 = [11,22,33]
list2.insert(-1,88)
print(list2)

# extend
list3 =[1,2]
list3.extend([44,55])
list3.extend('hello')
print(list3)
# --------------------------------修改
list4 =[ 1,2,3]
list4[1]=1.1
print(list4)
# ------------------------------查找
list5 =[1,'2',3,'hh']
# 索引取值
res5 = list5[2]
print(res5)
# 查找元素对饮索引
res6 = list5.index('2')
print(res6)
res7 =list5.count('hh')
print(res7)



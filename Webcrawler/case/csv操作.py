"""
@Time    : 2022/3/26 21:51
@Author  : feng
"""
import csv

# 创建及编写表头文件
with open(r'../file/test1.csv', mode='a', encoding='utf-8-sig', newline='') as f:
    csv_write = csv.writer(f)
    csv_write.writerow(['title', 'view', 'sales', 'pic_url'])

with open(r'../file/test1.csv', mode='a', encoding='utf-8-sig', newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow([1,2,3,4])

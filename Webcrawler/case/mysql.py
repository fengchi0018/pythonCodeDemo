import pymysql
import threading
import pymysql

# 创建连接
conn = pymysql.connect(host='150.158.103.95', port=3306, user='orange', passwd='fateu123', db='test_cece', charset='utf8')
# 创建游标, 查询数据默认为元组类型
db = conn.cursor()
# cursor.executemany("insert into goods(title, item_loc, view_sales,pic_url)values(%s, %s, %s,%s)", [("11", '333', 'ceshi3@11.com',""), ("ceshi4", '444', 'ceshi4@qq.com',"")])
sql = f'insert into goods(title, item_loc, view_sales, pic_url) values ("1","1","1","3")'
db.execute(sql)
# 提交，不然无法保存新建或者修改的数据
conn.commit()
# 关闭游标
db.close()
# 关闭连接
conn.close()

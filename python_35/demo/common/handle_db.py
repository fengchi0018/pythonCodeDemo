''''
@File  : handle_db.py
@Author: Feng
@Date  : 2022/4/13
@Desc  : 
'''
import pymysql


class HandleDB:
    def __init__(self):
        # 返回数据转化为list字典: cursorclass = pymysql.cursors.DictCursor
        self.con = pymysql.connect(host='150.158.103.95',
                                   port=3306,
                                   user='orange',
                                   password='fateu123',
                                   db='dev_fateu', charset='utf8',
                                   cursorclass=pymysql.cursors.DictCursor)

    def fina_all(self, sql):
        with self.con.cursor() as cur:
            cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        return res

    def fina_one(self, sql):
        with self.con.cursor() as cur:
            cur.execute(sql)
        res = cur.fetchone()
        cur.close()
        return res

    def fina_count(self, sql):
        with self.con.cursor() as cur:
            res = cur.execute(sql)
        cur.close()
        return res

    def __del__(self):
        self.con.close()


if __name__ == '__main__':
    db = HandleDB()
    sql = 'select * from goods'
    res = db.fina_all(sql)
    print(res)

"""
    con = pymysql.connect(host='150.158.103.95',
                          port=3306,
                          user='orange',
                          password='fateu123',
                          db='test_cece')
    sql = 'select * from goods'
    # 创建游标
    cur = con.cursor()
    # 执行sql
    cur.execute(sql)
    # 获取所有结果，返回元组类型
    res = cur.fetchall()
    print(res)
    # 关闭游标
    cur.close()
    # 关闭连接
    con.close()
"""

''''
@File  : test_login.py
@Author: Feng
@Date  : 2022/4/12
@Desc  : 
'''
import json
import os
import random
import unittest
from jsonpath import jsonpath
import requests
from unittestreport import ddt, list_data
from demo.common.handle_excel import HandExcel
from demo.common.handle_path import DATA_DIR
from demo.common.handle_conf import conf
from demo.common.handle_log import my_log
from demo.common.handle_db import HandleDB


@ddt
class TestLogin(unittest.TestCase):
    excel = HandExcel(os.path.join(DATA_DIR, '测试用例.xlsx'), 'login')
    cases = excel.read_data()
    headers = eval(conf.get('requests', 'headers'))
    ip = conf.get('requests', 'dev_ip')

    @list_data(cases)
    def test_login(self, item):
        if '#mobileTel#' in item["data"]:
            phone = self.creatPhone()
            item['data'] = item['data'].replace('#mobileTel#', phone)
        # 使用数据库查询该号码是否在数据库中
            print(phone)
            sql = "select * from `user` where `user`.mobile_tel={}".format(phone)
            db = HandleDB()
            if db.fina_count(sql) == 0:
                print("该号码未注册")
            else:
                print("该号码已注册")
        params = eval(item["data"])
        # 用例中expected：json数据中存在false值，该值在python中不存在
        false = False
        true = True
        expected = eval(item["expected"])
        method = item['method'].lower()
        url = self.ip + item['url']
        headers = self.headers

        responses = requests.request(method, url, data=params, headers=headers)
        res = responses.json()
        try:
            # self.assertEqual(res['code'], expected['code'])
            self.assertEqual(expected['code'], jsonpath(res, '$.code')[0])
        except AssertionError as e:
            my_log.exception(e)
            my_log.error("-----用例{}失败".format(item['title']))
            raise e
        else:
            my_log.info("-----用例%s成功" % (item['title']))

    # 生成手机号
    def creatPhone(self):
        # phone =str(random.randint(13300000001,13399999999))
        phone = '133'
        for i in range(8):
            n = str(random.randint(0, 9))
            phone = phone + n
        return phone

''''
@File  : test_compoundRecommend.py
@Author: Feng
@Date  : 2022/4/13
@Desc  : 
'''
import unittest
import os

import requests
from jsonpath import jsonpath
from unittestreport import ddt, list_data
from demo.common.handle_excel import HandExcel
from demo.common.handle_path import DATA_DIR
from demo.common.handle_conf import conf
from demo.common.handle_log import my_log


@ddt
class TestCompoundRecommend(unittest.TestCase):
    excel = HandExcel(os.path.join(DATA_DIR, '测试用例.xlsx'), 'compoundRecommend')
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls):
        user_params = {
            "mobileTel": conf.get('testDate', 'mobileTel'),
            "password": conf.get('testDate', 'password'),
        }
        header = eval(conf.get('requests', 'headers'))
        base_url = conf.get('requests', 'dev_ip')
        login_url = base_url + '/login'
        response = requests.post(url=login_url, data=user_params, headers=header)
        token = jsonpath(response.json(), '$..token')[0]
        header['Authorization'] = 'FateU ' + token
        cls.header = header

    @list_data(cases)
    def test_compoundRecommend(self, item):
        method = item['method'].lower()
        url = conf.get('requests', 'dev_ip') + item['url']
        params = eval(item['data'])
        true = True
        false = False
        expected = eval(item['expected'])
        response2 = requests.request(method, url, json=params, headers=self.header)
        try:
            self.asserDictIn(expected, response2.json())
        except AssertionError as e:
            my_log.error("----用例{}错误".format(item['title']))
            my_log.exception(e)
        else:
            my_log.info("-----用例{}通过".format(item['title']))

    # 成员判断
    def asserDictIn(self, excepted, res):
        for k, v in excepted.items():
            if res.get(k) == v:
                pass
            else:
                raise AssertionError("{} not in {}".format(excepted, res))

"""
@Time    : 2022/3/30 21:45
@Author  : feng
"""
import requests
import re
import json
import pprint
import csv
import datetime
import time

headers = {
    'Host': '182.131.1.150:9090',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
headers2 = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': '182.131.1.150:9090',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'Referer': 'http://182.131.1.150:9090/hydrologicDataTwo.html',
}
url = 'http://182.131.1.150:9090/hydrologicDataTwo.html'
info_url = 'http://182.131.1.150:9090/WaterInfo/getWaterInfoData'


def get_region():
    # 获取地区信息
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    data = re.findall("var orgs =(.*)]\r\n", html, re.S)[0]
    # split()返回list
    datas = data.replace('[', '').strip().replace(' ', '').split()
    list_data = []
    for data in datas:
        cases = {}
        code = data[data.find('"', 1, 8) + 1:data.find('n', 1, len(data)) - 2]
        name = data[data.find('name', 1, len(data)) + 6:len(data) - 3]
        cases = {"code": code, "name": name}
        # 字典加入list
        list_data.append(cases)
    return list_data


def creatFile(file_title):
    file_title_s = file_title
    with open(f'file/{file_title_s}.csv', mode='a', encoding='utf-8-sig', newline='') as f:
        print("新建", file_title, "成功")
        csv_write = csv.writer(f)
        csv_write.writerow(['地区', '日期', '时刻', '坝前水位', '入库流量', '出库'])


def saveData(file_title, RECORDDATE, RECORDQUARTER, WLUPSTREAM, WLDOWNSTREAM, FLOWOUT):
    file_title_s = file_title
    RECORDDATE_s = RECORDDATE
    RECORDQUARTER_s = RECORDQUARTER
    WLUPSTREAM_s = WLUPSTREAM
    WLDOWNSTREAM_s = WLDOWNSTREAM
    FLOWOUT_s = FLOWOUT
    with open(f'file/{file_title_s}.csv', mode='a', encoding='utf-8-sig', newline='') as f:
        csv_write = csv.writer(f)
        csv_write.writerow([file_title_s, RECORDDATE_s, RECORDQUARTER_s, WLUPSTREAM_s, WLDOWNSTREAM_s, FLOWOUT_s])

list_data_s = get_region()
    # 地区循环
for data in list_data_s:
    file_title = data['name']
    # 创建及编写表头文件
    creatFile(file_title)
    begin = datetime.date(2019, 1, 1)
    end = datetime.date(2021, 12, 31)
    d = begin
    delta = datetime.timedelta(days=1)
    # 日期循环
    while d <= end:
        date_f = d.strftime("%Y-%m-%d")
        data_s = {'orgCode': data['code'], 'date': date_f, 'type': 1}
        time.sleep(1)
        response = requests.post(info_url, headers=headers2, data=data_s)
        json_data = json.loads(response.text)
        datas = json_data['data']
        # 当天时刻循环
        try:
            for li in datas:
                RECORDDATE = li['RECORDDATE']
                RECORDQUARTER = li['RECORDQUARTER']
                WLUPSTREAM = li['WLUPSTREAM']
                WLDOWNSTREAM = li['WLDOWNSTREAM']
                FLOWOUT = li['FLOWOUT']
                saveData([file_title, RECORDDATE, RECORDQUARTER, WLUPSTREAM, WLDOWNSTREAM, FLOWOUT])
        except Exception as e:
            print(e)
        d += delta

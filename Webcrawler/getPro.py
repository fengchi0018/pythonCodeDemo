''''
@File  : getPro.py
@Author: Feng
@Date  : 2022/3/28
@Desc  : 快代理
'''
import requests
import re
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    'Host': 'www.kuaidaili.com'
}


def getpro():
    pro_all_list = []
    for i in range(1,4):
        time.sleep(3)
        url = f'https://www.kuaidaili.com/free/inha/{i}/'
        reponse = requests.get(url, headers=headers)
        html = reponse.text
        ip_list = re.findall(r'<td data-title="IP">(.*?)</td>', html)
        port_list = re.findall('<td data-title="PORT">(.*?)</td>', html)
        type_list = re.findall('<td data-title="类型">(.*?)</td>', html)
        for ip, port, type in zip(ip_list, port_list, type_list):
            ip_str = ip + ":" + port
            pro_dict = {
                "https": "http://" + ip_str,
                "http": "http://" + ip_str
            }
            pro_all_list.append(pro_dict)
    return pro_all_list


def check_ip(pro_all_list):
    pro_all_list = pro_all_list
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'Host': 'www.baidu.com'
    }
    check_url = "https://www.baidu.com/"
    pro_list = []
    for pro in pro_all_list:
        time.sleep(1)
        try:
            reponse = requests.get(check_url, headers=headers, proxies=pro,timeout=1)
            if (reponse.status_code == 200):
                print(pro,"可用")
                pro_list.append(pro)
            else:
                print("不可用")
        except Exception as e:
            print("异常不可用",e)
    return pro_list


if __name__ == '__main__':
    check_ip(getpro())

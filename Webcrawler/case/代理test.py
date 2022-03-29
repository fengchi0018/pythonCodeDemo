''''
@File  : 代理test.py
@Author: Feng
@Date  : 2022/3/24
@Desc  : 
'''
import requests

# url = 'https://www.ip.cn/api/index'
# params = {
#     'ip': '',
#     'type': '0'
# }
# headers = {
#     'referer': ' https://www.ip.cn/',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
# }
# pro = {
#     'https': '101.33.73.209',
# }
# response = requests.get(url, params=params, headers=headers, proxies=pro)
# print(response.text)

import requests

# 隧道域名:端口号
# tunnel = "tpsXXX.kdlapi.com:15818"

# 用户名密码方式
headers = {
    'Referer': 'https://www.baidu.com/s?wd=%E6%B5%8B%E8%AF%951&rsv_spt=1&rsv_iqid=0xdf264ed00003a5c4&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=68018901_7_pg&rsv_enter=0&rsv_dl=tb&oq=%25E6%25B5%258B%25E8%25AF%2595&rsv_btype=t&rsv_t=904fLqStLGrfccdhpTSHwWIIO4R8w5bg9aOHcVepwVRHTDrU1StLmadpp1osLfNSLSWs3A&rsv_pq=bec6210600037d75&inputT=1359&rsv_sug3=10&rsv_sug1=5&rsv_sug7=100&rsv_sug4=1992',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
}
proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}
target_url = "https://www.baidu.com"
try:
    response = requests.get(target_url, headers=headers, proxies=proxies)
    # 获取页面内容
    if response.status_code == 200:
        print(response.text)
except Exception as e:
    print(e)

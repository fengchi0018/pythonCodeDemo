''''
@File  : test2.py
@Author: Feng
@Date  : 2022/3/25
@Desc  : 
'''
from urllib import error
import random,requests
# 代理IP
proxies_list = [
    {'http':'47.57.188.208'},
    # { 'http':'47.242.200.148'}
]

url = 'http://www.baidu.com'
# 免费代理会失效，需要try
try:
    proxies = random.choice(proxies_list)
    print(proxies)
    rsp = requests.post(url,proxies=proxies)
    rsp.encoding='utf-8'
    html = rsp.text
    print(html)

except error.URLError as e:
    print(e)
except Exception as e:
    print(e)
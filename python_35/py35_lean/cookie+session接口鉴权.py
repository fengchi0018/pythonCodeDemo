''''
@File  : cookie+session接口鉴权.py
@Author: Feng
@Date  : 2022/4/8
@Desc  : 
'''
import requests
# 创建一个会话对象（使用session对象去发生请求，会自动记录请求的cookie信息，下一次请求自动化添加cookie
s = requests.session()
login_url = 'https://openapiv5.ketangpai.com//UserApi/login'
url = 'https://openapiv5.ketangpai.com//MessageApi/getNoReadMessageCount'
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'Referer': 'https://www.ketangpai.com/'
}
login_data = {
    "code": "",
    "email": "13540195370",
    "mobile": "",
    "password": "fengchi0218",
    "remember": "0",
    "reqtimestamp": 1649398226722,
    "type": "login"
}
login_response = s.post(url=login_url, json=login_data,headers=head)
print(login_response.json())
json = {
    'reqtimestamp': '1649397816538',
    'type': '100'
}
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'
}
response = s.post(url=url, json=json, headers=head)
print(response.json())

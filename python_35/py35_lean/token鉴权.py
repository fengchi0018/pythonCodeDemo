''''
@File  : token鉴权.py
@Author: Feng
@Date  : 2022/4/8
@Desc  : 
'''
import requests
import pprint

sendMessage_url = 'http://106.52.11.130:8085/admin/sendEmailLoginCode'
login_url = 'http://106.52.11.130:8085/admin/login'
list_url = ' http://106.52.11.130:8085/f/opus/list'
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'token': 'CNGCSCMPPSHYIDUNNIESHNRLBDRKHUHMXMXP',
}
send_params = {
    "username": "administrator"
}
sendMessage_response = requests.post(url=sendMessage_url, data=send_params, headers=head)
print(sendMessage_response.text)
login_params = {
    'username': 'administrator',
    'password': '10241024',
    'code': '123456'
}
login_response = requests.post(url=login_url, data=login_params, headers=head)
# login_response.json()将json数据直接转化为python数据类型
# pprint.pprint(login_response.json())
token = login_response.json()['data']['token']
print(token)
head2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'token': token,
}
list_params = {
    "userId": "",
    "opusId": "",
    "page": 1,
    "limit": 10,
    "opusType": "",
    "nickname": "",
    "title": "",
    "examineStatus": "",
    "startDate": "",
    "endDate": "",
}
list_response = requests.get(url=list_url, data=list_params, headers=head2)
pprint.pprint(list_response.json())

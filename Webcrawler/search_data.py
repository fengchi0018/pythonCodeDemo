"""
@Time    : 2022/3/30 21:45
@Author  : feng
"""
import requests
import re
import json

headers = {
    'Host': '182.131.1.150:9090',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
url = 'http://182.131.1.150:9090/hydrologicDataTwo.html'
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
html = response.text
data = re.findall("var orgs =(.*)]\r\n",html,re.S)[0]
datas = data.replace('[','').strip().replace(' ','').split()
code_list=[]
name_list=[]
cases=[]
print(datas[0])
cases=[]
for data in datas:
    
    json_d =json.loads(data)
    print(json_d)
    cases.append(json_d)


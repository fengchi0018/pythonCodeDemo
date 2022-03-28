''''
@File  : getPro.py
@Author: Feng
@Date  : 2022/3/28
@Desc  : 
'''
import requests
import re
headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'Host': 'www.kuaidaili.com'
    }
def getpro():
    url ='https://www.kuaidaili.com/free/'
    reponse = requests.get(url,headers=headers)
    html = reponse.text
    ip_list = re.findall(r'<td data-title="IP">(.*?)</td>', html)
    port_list = re.findall('<td data-title="PORT">(.*?)</td>', html)
    type_list = re.findall('<td data-title="类型">(.*?)</td>', html)
    pro_list =[]
    for ip,port,type in zip(ip_list,port_list,type_list):
        ip_str =ip+":"+port
        pro_dict={
            "https":"http://"+ip_str,
             "http": "http://"+ip_str
        }
        pro_list.append(pro_dict)
    return check_ip(pro_list)
def check_ip(pro_list):
    pro_list =pro_list
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'Host': 'www.baidu.com'
    }
    for pro in pro_list:
        check_url="https://www.baidu.com/"
        try:
            reponse = requests.get(check_url, headers=headers,proxies=pro)
            if (reponse.status_code ==200):
                print(pro+"可用")
                return pro
            else:
                print("不可用")
        except Exception as e:
            print("异常不可用")







if __name__ == '__main__':
    getpro()

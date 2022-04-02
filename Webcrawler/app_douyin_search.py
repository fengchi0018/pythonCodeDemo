''''
@File  : app_douyin_search.py
@Author: Feng
@Date  : 2022/4/2
@Desc  : 
'''
# 1.安装夜神android 5.X版本，并安装Xposed框架和JustTrustMe组件
# 2.安装mitmporxy工具     pip install mitmproxy       mitmdump --version 查看是否安装
# 3. cmd进入文件目录：mitmdump -s filename.py -p 8888
# 4.重启模拟器的软件，操作至接口功能处
import json
def reponses(flow):
    if '/aweme/v1/user/follower/list' in flow.request.url:
        for user in json.dump(flow.responses.txt)['followers']:
            douyin_info = {}
            douyin_info['nickname'] = user['nickname']
            # douyin_info['user_urged'] = ['urge_detail']['user_urged']
            print(douyin_info)


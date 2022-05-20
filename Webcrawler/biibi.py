# cmd = f"ffmpeg -i {video_name}.mp4 -i {video_name}.mp3 -c:v copy -c:a aac -strict experimental {video_name}output.mp4"
"""
b站视频下载：
ffmpeg下载配置系统环境
"""
import requests
import re
import pprint
import json
import subprocess
import os
import time

headers = {
    'referer': 'https://www.bilibili.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
}


# 搜索页面搜索相关视频
def search(keyword):
    url_bbid = 'https://api.bilibili.com/x/web-interface/search/type'
    data = {
        "context": "",
        'keyword': keyword,
        'page': '1',
        'order': '',
        'category_id': '',
        'duration': '1',
        'user_type': '',
        'order_sort': '',
        'tids_1': '',
        'tids_2': '',
        'search_type': 'video',
        'changing': 'id',
        '__refresh__': 'true',
        '__reload__': 'false',
        '_extra': '',
        'highlight': '1',
        'single_column': '0'
    }
    json_data1 = requests.get(url=url_bbid, params=data, headers=headers).json()
    return json_data1


# 获取视频id
def bvid_info(data):
    mv_data = data
    bvid_list = []
    for index in mv_data['data']['result'][1:]:
        time1 = index['duration']
        num = time1.find(':')
        start = time1[0:num]
        if int(start) > 1:
            continue
        else:
            bvid_list.append(index['bvid'])
    return bvid_list


# //获取选定视频
def go_mv(bv_id):
    time.sleep(3)
    bv_id = bv_id
    index_url = f'https://www.bilibili.com/video/{bv_id}'
    response = requests.get(url=index_url, headers=headers)
    # re.findall()查找
    # print(response.text)
    try:
        title_li = re.findall('<h1 id="video-title" title="(.*)" class ="video-title" >', response.text)
        if len(title_li) > 0:
            title = title_li[0].replace(' ', '')
            print('------------' + title + '--------------')
            html_data = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]
            json_data = json.loads(html_data)
            # 获取视频音频地址
            audio_url = json_data['data']['dash']['audio'][0]['backupUrl'][0]
            video_url = json_data['data']['dash']['video'][0]['backupUrl'][0]
            # 保存数据
            audio_content = requests.get(url=audio_url, headers=headers).content
            video_content = requests.get(url=video_url, headers=headers).content
            file_path = r"D:/PycharmProjects/Webcrawler/bibi_mv/{}".format(title)
            with open(file_path + '.mp3', mode='wb') as f:
                f.write(audio_content)
            with open(file_path + '.mp4', mode='wb') as f:
                f.write(video_content)
            # 视频音频合成
            cmd = f"ffmpeg -i D:/desk/bibi_mv/{title}.mp4 -i D:/desk/bibi_mv{title}.mp3 -c:v copy -c:a aac -strict experimental D:/desk/bibi_mv/{title}output.mp4"
            subprocess.run(cmd, shell=True)
            print('----------' + f'{title}已下载’+‘------------')
            # 移除原视频音频
            os.remove(f'{file_path}.mp3')
            os.remove(f'{file_path}.mp4')
        else:
            print("未获取到标题")
    except Exception as e:
        print("标题获取错误：",e)
        # title = re.findall('<h1 id="video-title" title="(.*)" class ="video-title" >', response.text)[0].replace(' ', '')




"""
    # 搜索页搜索并下载
    search_str = input("请输入关键词")
    search_response = search(search_str)
    list_mv_bvid = bvid_info(search_response)
    print(list_mv_bvid)
    for index in list_mv_bvid:
        try:
            go_mv(bv_id=index)
        except Exception as err:
            print("出错")
"""
# 输入bvid下载视频
while True:
    bvid_str = input("请输入bvid(输入0则停止):")
    if (bvid_str == '0'):
        break
    else:
        go_mv(bv_id=bvid_str)

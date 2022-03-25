"""
======================
Time:2022/3/23 11:37
Author:feng
========================
1.分析数据
2.获取数据：
          请求数据
          获取数据
          解析数据
          保存数据
          合成数据
"""
import requests
import re
import pprint
import json
import os
import subprocess

url = 'https://www.bilibili.com/video/BV1sQ4y1B716'
headers = {
    'referer': 'https://www.bilibili.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'

}
# 请求数据
reponse = requests.get(url=url, headers=headers)
# print(reponse.text)
# 查询数据
title = re.findall('<h1 title="(.*?)" class="video-title">', reponse.text, re.S)[0].replace(' ', '')
html_data = re.findall('<script>window.__playinfo__=(.*?)</script>', reponse.text, re.S)[0]
# 转为json
json_data = json.loads(html_data)
# 格式化打印
# pprint.pprint(json_data)
# 获取数据
audio_url = json_data['data']['dash']['audio'][0]['backupUrl'][0]
video_url = json_data['data']['dash']['video'][0]['backupUrl'][0]
# 保存数据
audio_content = requests.get(url=audio_url, headers=headers).content
video_content = requests.get(url=video_url, headers=headers).content
# 写入数据
file_path = r"D:/PycharmProjects/Webcrawler/bibi_mv/{}".format(title)
with open(file_path + '.mp3', mode='wb') as f:
    f.write(audio_content)
with open(file_path + '.mp4', mode='wb') as f:
    f.write(video_content)
cmd = f"ffmpeg -i D:/PycharmProjects/Webcrawler/bibi_mv/{title}.mp4 -i D:/PycharmProjects/Webcrawler/bibi_mv/{title}.mp3 -c:v copy -c:a aac -strict experimental D:/PycharmProjects/Webcrawler/bibi_mv/{title}output.mp4"
print(cmd)
subprocess.run(cmd, shell=True, encoding='utf-8')
os.remove(f'{file_path}.mp4')
os.remove(f'{file_path}.mp3')

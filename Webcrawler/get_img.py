"""
@Time    : 2022/6/6 20:48
@Author  : feng
网站：https://www.kanxiaojiejie.com/
"""
import requests
# 解析数据的模块
import parsel

index_url = 'https://www.kanxiaojiejie.com/'
response = requests.get(index_url)
html_data = response.text
select = parsel.Selector(html_data)
url_list = select.css('.entry-top a::attr(href)').getall()
for url in url_list:
    print(url)
    response = requests.get(url=url)
    html_data = response.text
    select = parsel.Selector(html_data)
    img_list = select.css('.entry-content img::attr(src)').getall()
    for img_url in img_list:
        response = requests.get(url=img_url)
        img_name = img_url.split('/')[-1]
        with open(f'img/{img_name}', mode='wb') as f:
            f.write(response.content)

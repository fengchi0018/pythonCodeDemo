import requests
import re
import json
import pprint
import csv
import time
import pymysql
from cffi.cparser import lock
'''
淘宝搜索页结果数据：
保存至csv文件/数据库
'''


def save_sql (title, item_loc, view_sales, pic_url):
    count = pymysql.connect(host='150.158.103.95',
                    port=3306,
                    user='orange',
                    password='fateu123',
                    db='test_cece')
    db = count.cursor()
    sql =f'insert into goods(title, item_loc, view_sales, pic_url) values ("{title}", "{item_loc}", "{view_sales}", "{pic_url}")'
    lock.acquire()
    db.execute(sql)
    lock.release()
    count.commit()
    db.close()
# 创建及编写表头文件
with open('file/淘宝.csv', mode='a', encoding='utf-8-sig', newline='') as f:
    csv_write = csv.writer(f)
    csv_write.writerow(['title', 'view', 'sales', 'pic_url'])
# 翻页：1，2页数据
for page in range(1,3):
    time.sleep(5)
    url =f'https://s.taobao.com/search?q=%E5%A5%B3%E8%A3%85&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=2%2C48&s={page * 44}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'referer': 'https://uland.taobao.com/',
        'cookie': 'cna=tTb2FsmYTT0CAdym5N3Y1ErG; enc=legBw%2BW3RCLQLiQ8tLLQFvvAeVell7TWIRuYnFM%2BNm56Vp6YCV1Ies9x%2FstGfumAdQszUjRmV%2F0wzZKBTeH2qw%3D%3D; _m_h5_tk=604be77516dbc44fa793116cebba050f_1648133339581; _m_h5_tk_enc=9035c0f6d7e08a80030b1905712c1bff; xlly_s=1; tfstk=cGclBjxy2Yy5LFwmCQNSuU1Y6U9Aw5pzVXlqgfKdCdlP2g1mwtWNOOL02htPd; l=eBSPdiulLIMPW8DfKOfanurza77OSIRYYuPzaNbMiOCP991B5Pt5W60LIh86C3GNhsi9R3WK4ADXBeYBqQAonxvtNSVsr4Dmn; isg=BCQkklu6Gqvdtm7niWErsLO-9SIWvUgn61sklT5FsO-y6cSzZs0Yt1pPqUlxNoB_'
    }
    responses = requests.get(url, headers=headers)
    html_data = re.findall("g_page_config =(.*);", responses.text)[0]
    # 字符串转json格式字典
    json_data = json.loads(html_data)
    auctions = json_data['mods']['itemlist']['data']['auctions']
    countnum=len(auctions)
    try:
        for auction in auctions[1:2]:
            title = auction['title']
            item_loc = auction['item_loc']
            view_sales = auction['view_sales']
            pic_url = auction['pic_url']
            save_sql(title, item_loc, view_sales, pic_url)
            # with open('淘宝.csv', mode='a', encoding='utf-8-sig', newline='') as f:
            #     csv_write = csv.writer(f)
            #     csv_write.writerow([title, item_loc, view_sales, pic_url])
    except Exception as e:
        print(e)
        pass

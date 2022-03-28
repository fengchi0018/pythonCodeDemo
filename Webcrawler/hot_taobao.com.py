import requests
import re
import json
import pprint
import csv
import time
# 创建及编写表头文件
with open('淘宝hot.csv', mode='a', encoding='utf-8-sig', newline='') as f:
    csv_write = csv.writer(f)
    csv_write.writerow(['title', 'view', 'sales', 'pic_url'])
# 翻页：1，2页数据
# for page in range(1,2):
#     time.sleep(5)
    url =f'https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword=%E8%A1%A3%E6%9C%8D&clk1=33325531bb9c7521953655c21a922d1a&upsId=33325531bb9c7521953655c21a922d1a&spm=a2e0b.20350158.31919782.1&pid=mm_26632258_3504122_32538762&union_lens=recoveryid%3A201_33.51.64.102_24410778_1648132887779%3Bprepvid%3A201_33.51.64.102_24410778_1648132887779&pnum=1'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        'referer': 'https://uland.taobao.com/',
        'cookie': 'cna=tTb2FsmYTT0CAdym5N3Y1ErG; enc=legBw%2BW3RCLQLiQ8tLLQFvvAeVell7TWIRuYnFM%2BNm56Vp6YCV1Ies9x%2FstGfumAdQszUjRmV%2F0wzZKBTeH2qw%3D%3D; _m_h5_tk=604be77516dbc44fa793116cebba050f_1648133339581; _m_h5_tk_enc=9035c0f6d7e08a80030b1905712c1bff; xlly_s=1; tfstk=cGclBjxy2Yy5LFwmCQNSuU1Y6U9Aw5pzVXlqgfKdCdlP2g1mwtWNOOL02htPd; l=eBSPdiulLIMPW8DfKOfanurza77OSIRYYuPzaNbMiOCP991B5Pt5W60LIh86C3GNhsi9R3WK4ADXBeYBqQAonxvtNSVsr4Dmn; isg=BCQkklu6Gqvdtm7niWErsLO-9SIWvUgn61sklT5FsO-y6cSzZs0Yt1pPqUlxNoB_'
    }
    responses = requests.get(url, headers=headers)
    print(responses.text)
    html_data = re.findall("mtopjsonp2((.*))", responses.text)[0]
    # 字符串转json格式字典
    json_data = json.loads(html_data)
    pprint.pprint(json_data)
    # auctions = json_data['mods']['itemlist']['data']['auctions']
    # try:
    #     for auction in auctions:
    #         title = auction['title']
    #         item_loc = auction['item_loc']
    #         view_sales = auction['view_sales']
    #         pic_url = auction['pic_url']
    #         with open('淘宝.csv', mode='a', encoding='utf-8-sig', newline='') as f:
    #             csv_write = csv.writer(f)
    #             csv_write.writerow([title, item_loc, view_sales, pic_url])
    # except Exception as e:
    #     print(e)
    #     pass

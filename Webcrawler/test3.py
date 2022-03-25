''''
@File  : test3.py
@Author: Feng
@Date  : 2022/3/25
@Desc  : 
'''
# json序列化，反序列化
url = "https://c0.3.cn/stock?skuId=12464037&cat=1713,3259,3333&venderId=1000077923&area" \
      "=4_113_9786_0&buyNum=1&choseSuitSkuIds=&extraParam={%22originid%22:%221%22}&ch=1&fqsp=0&" \
      "pduid=1573698619147398205303&pdpin=jd_635f3b795bb1c&coord=&detailedAdd=&callback=jQuery6495921"
# 倒叙[-1],切割
jQuery_id = url.split("=")[-1] + "("
# jQuery6495921(
print(jQuery_id)
# response.text.replace(jQuery_id, "")[:-1]


# 切片
s = 'ASTRING'
# s[:-1]  # 'ASTRIN'
# s[:len(s) - 1] # 'ASTRIN'
# s[0:len(s) - 1]  # 'ASTRIN'
print(s[:-2])
print(s[:len(s) - 2])
print(s[0:len(s) - 2])

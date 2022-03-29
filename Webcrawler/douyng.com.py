''''
@File  : douyng.com.py
@Author: Feng
@Date  : 2022/3/29
@Desc  : 
'''
import requests
import re

url = 'https://www.douyin.com/video/7080131170075299086'
headers = {
    'cookie':
        '__ac_nonce=06242bd56008880571b27; __ac_signature=_02B4Z6wo00f01HTI6rwAAIDBF8Iq1QNIYTR06O4AAH947f; ttwid=1%7C0qn5HbTIakR5H9Kaiai6EM07Bq58QAGRCCmxS-8U5d4%7C1648541014%7C310b6b7ad3fee4e7e9299b9f131108d650777a8770b7332dd75cb274d35ef883; _tea_utm_cache_6383=undefined; douyin.com; strategyABtestKey=1648541017.269; passport_csrf_token=40ced96c87bc6d754a49ba0a9633f96c; passport_csrf_token_default=40ced96c87bc6d754a49ba0a9633f96c; s_v_web_id=verify_l1burakr_i84jGJKY_5avL_49ZT_BzlW_d7ZzkZTClAuM; AB_LOGIN_GUIDE_TIMESTAMP=1648541017157; MONITOR_WEB_ID=cf20faef-bd82-441e-9995-729c9d00ff11; _tea_utm_cache_1300=undefined; msToken=2Kj5sLrnFTBe1LY97dKBEClv8EiKdOo3AU72MVhjgLCAy8O64YhYcOPwZ_6qemitbBb7rJQ3eSF9uTRJaDOs3_OFN3s-rOabIRp5CmXbxvl0Bxn4sh7EOw==; ttcid=2ce8f4f4a12f42bfb5b8560003387f6118; tt_scid=54jVJhCBC9bA1whHci2ZuoJW9KlBbP7zYVJgG5HrZiMpbBUuRzy835V1f7g1hod-c59e; THEME_STAY_TIME=54010; msToken=qjD1vNjKXcPc8nz_YWBCCd_e43SLTdoh2L58itnablQaInC-j4ECj-CWHgV2mxabrWTQM-rkYUa9LRNqjpKzlUWBUWdfZLIBt5SRW1t3kFAuGHT36dLfzQ==; home_can_add_dy_2_desktop=0',
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    'referer': 'https://www.douyin.com/'
}
response = requests.get(url, headers=headers)
data = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script>', response.text)[0]
print(data)

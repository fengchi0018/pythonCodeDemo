''''
@File  : read_yaml.py
@Author: Feng
@Date  : 2022/4/1
@Desc  : 
'''

import yaml
f = open('test.yaml', 'r', encoding='utf-8')
data = f.read()
f.close()
all_data = yaml.load_all(data,Loader=yaml.FullLoader)
for data in all_data:
    # data字典
    print(data)
    print(data['address'][0]['street'])


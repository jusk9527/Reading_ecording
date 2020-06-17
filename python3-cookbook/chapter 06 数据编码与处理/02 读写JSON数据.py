# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     02
   Description :
   Author :       jusk?
   date：          2019/12/4
-------------------------------------------------
   Change Activity:
                   2019/12/4:
-------------------------------------------------
"""

# 读写JSON数据

import json

data = {
    'name' : 'ACME',
    'shares' : 100,
    'price' : 542.23
}

json_str = json.dumps(data)
print(json)

rs = json.loads(json_str)
print(rs)

# <module 'json' from 'C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python36\\lib\\json\\__init__.py'>
# {'name': 'ACME', 'shares': 100, 'price': 542.23}

# Writing JSON data
with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)

# JSON编码支持的基本数据类型为 None ， bool ， int ， float 和 str

s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)

# OrderedDict([('name', 'ACME'), ('shares', 50), ('price', 490.1)])
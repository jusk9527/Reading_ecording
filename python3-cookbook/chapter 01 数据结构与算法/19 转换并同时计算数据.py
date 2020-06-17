# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     19 转换并同时计算数据
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# -- 你需要在数据序列上执行聚集函数（比如 sum() , min() , max() ）， 但是首先你需要先转换或者过滤数据

## -- 一个非常优雅的方式去结合数据计算与转换就是使用一个生成器表达式参数。 比如，如果你想计算平方和，可以像下面这样做

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)
# 55

import os
files = os.listdir('./')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')


# There be python!



s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))
# ACME,50,123.45

# Data reduction across fields of a data structure
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)

print(min_shares)
# 20



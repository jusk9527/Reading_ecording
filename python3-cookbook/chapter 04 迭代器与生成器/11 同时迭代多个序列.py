# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     11
   Description :
   Author :       jusk?
   date：          2019/12/3
-------------------------------------------------
   Change Activity:
                   2019/12/3:
-------------------------------------------------
"""

# 同时迭代多个序列
## 迭代长度跟参数中最短序列长度一致。zip取其短一端
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62,99]
for x, y in zip(xpts, ypts):
    print(x,y)
# 1 101
# 5 78
# 4 37
# 2 15
# 10 62
# 7 99



## 迭代长度跟参数中最短序列长度不一致。


a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
from itertools import zip_longest
for i in zip_longest(a,b):
    print(i)

# (1, 'w')
# (2, 'x')
# (3, 'y')
# (None, 'z')


for i in zip_longest(a, b, fillvalue=0):
    print(i)

# (1, 'w')
# (2, 'x')
# (3, 'y')
# (0, 'z')
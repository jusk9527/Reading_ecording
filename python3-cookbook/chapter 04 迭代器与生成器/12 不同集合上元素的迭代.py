# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     12
   Description :
   Author :       jusk?
   date：          2019/12/3
-------------------------------------------------
   Change Activity:
                   2019/12/3:
-------------------------------------------------
"""
# 不同集合上元素的迭代

from itertools import chain
a = [1,2,3,4,5]
b = ['x','y','z']
for x in chain(a,b):
    print(x)

# 1
# 2
# 3
# 4
# 5
# x
# y
# z
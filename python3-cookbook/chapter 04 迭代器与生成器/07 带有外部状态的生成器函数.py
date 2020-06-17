# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     07
   Description :
   Author :       jusk?
   date：          2019/12/3
-------------------------------------------------
   Change Activity:
                   2019/12/3:
-------------------------------------------------
"""

# 迭代器切片
import itertools
def count(n):
    while True:
        yield n
        n +=1
c = count(0)


for x in itertools.islice(c, 10,20):
    print(x)

# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
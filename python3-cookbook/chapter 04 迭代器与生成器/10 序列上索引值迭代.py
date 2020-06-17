# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     10
   Description :
   Author :       jusk?
   date：          2019/12/3
-------------------------------------------------
   Change Activity:
                   2019/12/3:
-------------------------------------------------
"""

# 序列上索引值迭代

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

# 0 a
# 1 b
# 2 c


# 为了按传统行号输出(行号从1开始)，你可以传递一个开始参数：
for idx, val in enumerate(my_list, 2):
    print(idx,val)

# 2 a
# 3 b
# 4 c
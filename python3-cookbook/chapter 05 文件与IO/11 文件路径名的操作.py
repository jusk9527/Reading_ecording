# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     11
   Description :
   Author :       jusk?
   date：          2019/12/4
-------------------------------------------------
   Change Activity:
                   2019/12/4:
-------------------------------------------------
"""

# 文件路径名的操作

import os
path = '/Users/beazley/Data/data.csv'
rs = os.path.basename(path)
print(rs)
# data.csv

rs = os.path.dirname(path)
print(rs)
# /Users/beazley/Data


rs = os.path.join('tmp', 'data', os.path.basename(path))
print(rs)
# tmp\data\data.csv

path = '~/Data/data.csv'
rs = os.path.expanduser(path)
print(rs)

# C:\Users\Administrator/Data/data.csv
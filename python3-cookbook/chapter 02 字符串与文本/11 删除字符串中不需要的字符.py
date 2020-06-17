# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     11
   Description :
   Author :       jusk?
   date：          2019/12/2
-------------------------------------------------
   Change Activity:
                   2019/12/2:
-------------------------------------------------
"""

# 删除字符串中不需要的字符\
s = ' hello world \n'
rs = s.strip()
print(rs)

# hello world

rs = s.lstrip()
print(rs)
#  hello world          留意有换行
#

rs = s.rstrip()
print(rs)
#  hello world

s = ' hello     world \n'
rs = s.strip()
print(rs)

# hello     world
rs = s.replace(' ', '')
print(rs)
# helloworld

# 读取多行数据

with open('filename') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     01
   Description :
   Author :       jusk?
   date：          2019/12/2
-------------------------------------------------
   Change Activity:
                   2019/12/2:
-------------------------------------------------
"""

# 手动遍历迭代器

l = [1,2,3]
m = iter(l)
print(next(m))
print(next(m))
print(next(m))
print(next(m))


# 1
# 2
# 3
# Traceback (most recent call last):
#   File "C:/Users/Administrator/Desktop/准备/python3-cookbook/chapter 04 迭代器与生成器/01 使用多个界定符分割字符串.py", line 21, in <module>
#     print(next(m))
# StopIteration
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     chapter 02 字符串与文本
   Description :
   Author :       jusk?
   date：          2019/12/2
-------------------------------------------------
   Change Activity:
                   2019/12/2:
-------------------------------------------------
"""

def deque(a):
    seen = set()
    for i in a:
        if i not in seen:
            yield i
            seen.add(i)


a = [1,3,5,9,6,2,1,3]

res = deque(a)
print(list(res))
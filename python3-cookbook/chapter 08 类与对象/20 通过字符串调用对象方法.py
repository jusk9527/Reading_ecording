# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     20 通过字符串调用对象方法
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# -- 你有一个字符串形式的方法名称，想通过它调用某个对象的对应方法。

## -- 最简单的情况，可以使用 getattr() ：


import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


p = Point(2, 3)

d = getattr(p, 'distance')(0, 0)

print(d)
# 3.605551275463989
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     17 创建不调用init方法的实例
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# -- 你想创建一个实例，但是希望绕过执行 __init__() 方法。

## -- 可以通过 __new__() 方法创建一个未初始化的实例。例如考虑如下这个类：

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


d = Date.__new__(Date)
d

data = {'year':2012, 'month':8, 'day':29}

for key, value in data.items():
    setattr(d, key, value)
print(d.year)

# 2012
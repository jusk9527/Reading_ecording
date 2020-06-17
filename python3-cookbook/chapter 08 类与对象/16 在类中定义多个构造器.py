# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     16 在类中定义多个构造器
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# -- 你想实现一个类，除了使用 __init__() 方法外，还有其他方式可以初始化它。

## -- 为了实现多个构造器，你需要使用到类方法

import time

class Date:
    """方法一：使用类方法"""
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


a = Date(2012, 12, 21)
b = Date.today()
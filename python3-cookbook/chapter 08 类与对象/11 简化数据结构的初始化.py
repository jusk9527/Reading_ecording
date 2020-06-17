# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     11 简化数据结构的初始化
   Description :
   Author :       jusk?
   date：          2019/12/31
-------------------------------------------------
   Change Activity:
                   2019/12/31:
-------------------------------------------------
"""

# -- 你写了很多仅仅用作数据结构的类，不想写太多烦人的 __init__() 函数

## -- 可以在一个基类中写一个公用的 __init__() 函数：


import math

class Structure1:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)



## -- 然后使你的类继承自这个基类:

# Example class definitions
class Stock(Structure1):
    _fields = ['name', 'shares', 'price']

class Point(Structure1):
    _fields = ['x', 'y']

class Circle(Structure1):
    _fields = ['radius']

    def area(self):
        return math.pi * self.radius ** 2

s = Stock('ACME', 50, 91.1)

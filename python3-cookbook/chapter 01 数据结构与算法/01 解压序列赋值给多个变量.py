# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     01 解压序列赋值给多个变量
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# -- 现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量？


## -- 任何的序列（或者是可迭代对象）可以通过一个简单的赋值语句解压并赋值给多个变量。
## -- 唯一的前提就是变量的数量必须跟序列元素的数量是一样的。


p = (4,5)
x,y = p
print(x)
# 4

print(y)
# 5

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]

name, shares, price, data = data

print(name)
# ACME

print(data)
# (2012, 12, 21)




name1, shares1, price1, (year1, mon1, day1) = [ 'ACME', 50, 91.1, (2012, 12, 21) ]

print(name1)
# ACME

print(year1)
# 2012

print(mon1)
# 12

print(day1)
# 21




"""
不仅仅是元组，包括字符串，文件对象，迭代器和生成器。
"""


s = 'Hello'

a, b,c,d,e = s

print(a)
# H

print(b)
# e
print(e)
# o



# -- 有时候，你可能只想解压一部分，丢弃其他的值。对于这种情况 Python 并没有提供特殊的语法。
# -- 但是你可以使用任意变量名去占位，到时候丢掉这些变量就行了。



data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]

_, shares2, price2, _ = data

print(shares2)
# 50
print(price)
# 91.1
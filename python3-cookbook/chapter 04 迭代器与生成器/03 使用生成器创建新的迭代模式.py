# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     03
   Description :
   Author :       jusk?
   date：          2019/12/3
-------------------------------------------------
   Change Activity:
                   2019/12/3:
-------------------------------------------------
"""


# -- 你想实现一个自定义迭代模式，跟普通的内置函数比如 range() , reversed() 不一样。


## -- 如果你想实现一种新的迭代模式，使用一个生成器函数来定义它。 下面是一个生产某个范围内浮点数的生成器：





def frange(start, stop, increment):
    x = start
    while x<stop:
        yield x
        x += increment

for n in frange(0,4,0.5):
    print(n)

# 0
# 0.5
# 1.0
# 1.5
# 2.0
# 2.5
# 3.0
# 3.5


def countdown(n):
    print("starting to count from", n)
    while n>0:
        yield n
        n-=1
    print("Done!")



c = countdown(3)
print(c)
# <generator object countdown at 0x00000000020ECE08>



rs = next(c)
print(rs)

# starting to count from 3
# 3

rs = next(c)
print(rs)
# 2

rs = next(c)
print(rs)
# 1

rs = next(c)
print(rs)

# Done!
# Traceback (most recent call last):
#   File "C:/Users/Administrator/Desktop/准备/python3-cookbook/chapter 04 迭代器与生成器/03 用Shell通配符匹配字符串.py", line 65, in <module>
#     rs = next(c)
# StopIteration


## 我们在迭代中通常使用的for语句会自动处理这些细节
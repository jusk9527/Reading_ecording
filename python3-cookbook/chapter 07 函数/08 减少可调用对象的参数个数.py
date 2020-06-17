# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     08 减少可调用对象的参数个数
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# -- 你有一个被其他python代码使用的callable对象，可能是一个回调函数或者是一个处理器，
# -- 但是它的参数太多了，导致调用时出错。

## -- 如果需要减少某个函数的参数个数，你可以使用 functools.partial() 。
## -- partial() 函数允许你给一个或多个参数设置固定的值，减少接下来被调用时的参数个数。
## -- 为了演示清楚，假设你有下面这样的函数：



def spam(a, b, c, d):
    print(a, b, c, d)


from functools import partial
s1 = partial(spam, 1) # a = 1
res_s1 = s1(2, 3, 4)
print(res_s1)
# 1 2 3 4


s3 = partial(spam, 1, 2, d=42)          # a = 1, b = 2, d = 42
print(s3(3))
# 1 2 3 42

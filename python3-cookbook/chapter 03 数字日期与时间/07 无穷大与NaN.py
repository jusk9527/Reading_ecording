# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     07 无穷大与NaN
   Description :
   Author :       jusk?
   date：          2019/12/30
-------------------------------------------------
   Change Activity:
                   2019/12/30:
-------------------------------------------------
"""

# -- 你想创建或测试正无穷、负无穷或NaN(非数字)的浮点数

## -- Python并没有特殊的语法来表示这些特殊的浮点值，但是可以使用 float() 来创建它们

a = float('inf')

b = float('-inf')

c = float('nan')


print(a)
# inf
print(b)
# -inf
print(c)
# nan


## -- 为了测试这些值的存在，使用 math.isinf() 和 math.isnan() 函数
import math

res_a = math.isinf(a)
print(res_a)
# True


res_nan = math.isnan(c)
print(res_nan)
# True


## 自己很少用到就往下了
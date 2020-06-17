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

# -- 你想对浮点数执行指定精度的舍入运算。



## 对于简单的舍入运算，使用内置的 round(value, ndigits) 函数即可
res = round(1.23,1)
print(res)
# 1.2

res = round(1.27,1)
print(res)
# 1.3
res = round(-1.27, 1)
print(res)
# -1.3

res = round(1.25361,3)
print(res)
# 1.254



## -- 传给 round() 函数的 ndigits 参数可以是负数，这种情况下，
## -- 舍入运算会作用在十位、百位、千位等上面
a = 1627731
res = round(a, -1)
print(res)

# 1627730

res = round(a, -2)
print(res)

# 1627700

res = round(a, -3)
print(res)
# 1628000


## 不要将四舍五入与格式化输出搞混淆了
## 仅仅只需要在格式化的时候指定精度即可
x = 1.23456
res = format(x, '0.2f')
print(res)
# 1.23
res = format(x, '0.3f')
print(res)
# 1.235

res = 'value is {:0.3f}'.format(x)
print(res)
# value is 1.235

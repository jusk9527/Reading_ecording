# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     08 字典的运算
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# -- 怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）


prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}



## -- 为了对字典值执行计算操作，通常需要使用 zip() 函数先将键和值反转过来

## -- min计算的是key值
min_price = min(zip(prices.values(), prices.keys()))

print(min_price)
# (10.75, 'FB')


max_price = max(zip(prices.values(), prices.keys()))

print(max_price)
# (612.78, 'AAPL')

## -- 可以使用 zip() 和 sorted() 函数来排列字典数据：
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
# [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]



## ---------------------------------------------------------------
## 思考


min(prices.values()) # Returns 10.75
max(prices.values()) # Returns 612.78

# ---------------------------------------------------------------
min(prices, key=lambda k: prices[k]) # Returns 'FB'
max(prices, key=lambda k: prices[k]) # Returns 'AAPL'

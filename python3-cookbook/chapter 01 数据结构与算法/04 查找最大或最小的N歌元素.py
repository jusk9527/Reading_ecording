# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     04 查找最大或最小的N歌元素
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# -- 怎样从一个集合中获得最大或者最小的 N 个元素列表？

## -- 解决方案 heapq 模块有两个函数：nlargest() 和 nsmallest() 可以完美解决这个问题。

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# 求最大值3项
print(heapq.nlargest(3, nums))

# [42, 37, 23]



# 求最小值3项
print(heapq.nsmallest(3, nums))
# [-4, 1, 2]



# 两个函数都能接受一个关键字参数，用于更复杂的数据结构中

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])


# 求价格最小的3项
print(cheap)

# [{'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75}]

expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])


# 求价格最大的3项
print(expensive)

# [{'name': 'AAPL', 'shares': 50, 'price': 543.22}, {'name': 'ACME', 'shares': 75, 'price': 115.65}, {'name': 'IBM', 'shares': 100, 'price': 91.1}]



nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
import heapq
heap = list(nums)
heapq.heapify(heap)

# 堆数据结构最重要的特征是 heap[0] 永远是最小的元素
print(heap)
[-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]

first = heapq.heappop(heap)
print(first)
# -4

second = heapq.heappop(heap)
print(second)
# 1

third = heapq.heappop(heap)
print(third)
# 2




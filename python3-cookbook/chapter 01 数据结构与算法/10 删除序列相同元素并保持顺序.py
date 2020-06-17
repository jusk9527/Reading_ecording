# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     10 删除序列相同元素并保持顺序
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""
# -- 怎样在一个序列上面保持元素顺序的同时消除重复的值？

## -- 如果序列上的值都是 hashable 类型，那么可以很简单的利用集合或者生成器来解决这个问题。比如：



## -- 列表
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
res_one = list(dedupe(a))
print(res_one)
# [1, 5, 2, 9, 10]


## -- 字典
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
res_two = list(dedupe(a, key=lambda d: (d['x'],d['y'])))
print(res_two)
# [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]


res_three = list(dedupe(a, key=lambda d: d['x']))
print(res_three)
# [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

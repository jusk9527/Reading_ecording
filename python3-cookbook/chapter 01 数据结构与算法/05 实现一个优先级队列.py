# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     05 实现一个优先级队列
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# -- 怎样实现一个按优先级排序的队列？
# 并且在这个队列上面每次 pop 操作总是返回优先级最高的那个元素

## 解决方案--下面的类利用 heapq 模块实现了一个简单的优先级队列：

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({!r})".format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 1)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

rs_first = q.pop()
print(rs_first)
# Item('spam')
re_second = q.pop()
print(re_second)
# Item('foo')
re_third = q.pop()
print(re_third)
# Item('bar')


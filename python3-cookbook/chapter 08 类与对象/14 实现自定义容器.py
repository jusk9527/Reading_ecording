# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     14 实现自定义容器
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# 你想实现一个自定义的类来模拟内置的容器类功能，
# 比如列表和字典。但是你不确定到底要实现哪些方法


# collections 定义了很多抽象基类，当你想自定义容器类的时候它们会非常有用。
# 比如你想让你的类支持迭代，那就让你的类继承 collections.Iterable 即可


import collections
class A(collections.Iterable):
    pass

# a = A()

# 不过你需要实现 collections.Iterable 所有的抽象方法
# TypeError: Can't instantiate abstract class A with abstract methods __iter__


# 这里面使用到了 bisect 模块，它是一个在排序列表中插入元素的高效方式。可以保证元素插入后还保持顺序。
import bisect
class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)


items = SortedItems([5, 1, 3])
print(list(items))
# [1, 3, 5]

print(items[0], items[-1])
# 1 5

items.add(2)
print(list(items))
# [1, 2, 3, 5]




# collections 中很多抽象类会为一些常见容器操作提供默认的实现

class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, index):
        print('Getting:', index)
        return self._items[index]

    def __setitem__(self, index, value):
        print('Setting:', index, value)
        self._items[index] = value

    def __delitem__(self, index):
        print('Deleting:', index)
        del self._items[index]

    def insert(self, index, value):
        print('Inserting:', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('Len')
        return len(self._items)

# 如果你创建 Items 的实例，你会发现它支持几乎所有的核心列表方法(如append()、remove()、count()等)

a = Items([1, 2, 3])
print(len(a))
# Len
# 3

a.append(4)
# Len
# Inserting: 3 4

a.count(2)
# Getting: 0
# Getting: 1
# Getting: 2
# Getting: 3
# Getting: 4


a.remove(3)

# Getting: 0
# Getting: 1
# Getting: 2
# Deleting: 2
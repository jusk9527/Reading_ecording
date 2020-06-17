# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     循环应用数据结构的内存管理
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# 你的程序创建了很多循环引用数据结构(比如树、图、观察者模式等)，你碰到了内存管理难题

# 一个简单的循环引用数据结构例子就是一个树形结构，
# 双亲节点有指针指向孩子节点，孩子节点又返回来指向双亲节点。 这种情况下，可以考虑使用 weakref 库中的弱引用。例如：


import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)

    # property that manages the parent as a weak-reference
    @property
    def parent(self):
        return None if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


root = Node('parent')
c1 = Node('child')
root.add_child(c1)
print(c1.parent)
# Node('parent')
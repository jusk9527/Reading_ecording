# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     原型模式
   Description :
   Author :       jusk?
   date：          2019/11/26
-------------------------------------------------
   Change Activity:
                   2019/11/26:
-------------------------------------------------
"""

import copy


class A:
    def __init__(self):
        self.x = 18
        self.msg = 'Hello'


class B(A):
    def __init__(self):
        A.__init__(self)
        self.y = 34
    def __str__(self):
           return '{}, {}, {}'.format(self.x, self.msg, self.y)


if __name__ == '__main__':
    b = B()
    c = copy.deepcopy(b)
    print([str(i) for i in (b, c)])
    print([i for i in (b, c)])


# ['18, Hello, 34', '18, Hello, 34']
# [<__main__.B object at 0x000000000283CAC8>, <__main__.B object at 0x000000000285A710>]


import copy
from collections import OrderedDict


class Book:
    def __init__(self, name, authors, price, **rest):
       '''Examples of rest: publisher, length, tags, publication
       date'''
       self.name = name
       self.authors = authors
       self.price = price      # in US dollars
       self.__dict__.update(rest)
    def __str__(self):
       mylist=[]
       ordered = OrderedDict(sorted(self.__dict__.items()))
       for i in ordered.keys():
           mylist.append('{}: {}'.format(i, ordered[i]))
           if i == 'price':
               mylist.append('$')
           mylist.append('\n')
       return ''.join(mylist)


class Prototype:
    def __init__(self):
       self.objects = dict()
    def register(self, identifier, obj):
       self.objects[identifier] = obj
    def unregister(self, identifier):
       del self.objects[identifier]
    def clone(self, identifier, **attr):
       found = self.objects.get(identifier)
       if not found:
           raise ValueError('Incorrect object identifier:{}'.format(identifier))
       obj = copy.deepcopy(found)
       obj.__dict__.update(attr)
       return obj


def main():
       b1 = Book('The C Programming Language', ('Brian W. Kernighan',
       'Dennis M.Ritchie'), price=118, publisher='Prentice Hall',
       length=228, publication_date='1978-02-22', tags=('C',
       'programming', 'algorithms', 'data structures'))
       prototype = Prototype()
       cid = 'k&r-first'
       prototype.register(cid, b1)
       b2 = prototype.clone(cid, name='The C Programming Language (ANSI)', price=48.99, length=274,
       publication_date='1988-04-01', edition=2)
       for i in (b1, b2):
           print(i)
       print("ID b1 : {} != ID b2 : {}".format(id(b1), id(b2)))


if __name__ == '__main__':
   main()
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     09 查找两字典的相同点
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# -- 怎样在两个字典中寻寻找相同点（比如相同的键、相同的值等等）？

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

## -- 为了寻找两个字典的相同点，可以简单的在两字典的 keys() 或者 items() 方法返回结果上执行集合操作

## 查找两个字典共同的key值
com_ab = a.keys() & b.keys()
print(com_ab)
# {'y', 'x'}

## 查找key值 在a 但是不在b
a_ab = a.keys() - b.keys()
print(a_ab)
# {'z'}


## 查找(key, value) 在ab共同
ab_ab = a.items() & b.items()
print(ab_ab)
# {('y', 2)}


## 把某些键去掉，编一本新字典
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)
# {'y': 2, 'x': 1}
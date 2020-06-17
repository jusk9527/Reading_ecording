# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     09
   Description :
   Author :       jusk?
   date：          2019/12/4
-------------------------------------------------
   Change Activity:
                   2019/12/4:
-------------------------------------------------
"""

# -- 你想创建一个新的拥有一些额外功能的实例属性类型，比如类型检查。

## -- 如果你想创建一个全新的实例属性，
## -- 可以通过一个描述器类的形式来定义它的功能。下面是一个例子：

# Descriptor attribute for an integer type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print("dd")
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

class Point:
    x = Integer('x')
    y = Integer('y')

    m = "ddd"

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __new__(cls, *args, **kwargs):
        print(cls)
        print(args[0])
        print(args)
        print(kwargs)
        return cls

p = Point(2, 3)
print(p.x)
print(p.m)


# <class '__main__.Point'>
# 2
# (2, 3)
# {}
# dd
# <__main__.Integer object at 0x00000000021A2C18>
# ddd


# 自己测试下效果
class User():
    def __init__(self,name,age):
        self.name = "dd"
        self.age = "c"

    def __get__(self, instance, owner):
        print("dd")

    def __set__(self, instance, value):
        print("dz")

class C():
    def __init__(self):
       pass

    user = User("xiao",13)
c = C()
c.user
c.user = "xiah"

# dd
# dz
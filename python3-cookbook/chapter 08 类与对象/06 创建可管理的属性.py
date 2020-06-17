# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     06
   Description :
   Author :       jusk?
   date：          2019/12/5
-------------------------------------------------
   Change Activity:
                   2019/12/5:
-------------------------------------------------
"""


# -- 你想给某个实例attribute增加除访问与修改之外的其他处理逻辑，
# -- 比如类型检查或合法性验证



## -- 创建可管理的属性
## -- 你想给某个实例attribute增加除访问与修改之外的其他处理逻辑，
## -- 比如类型检查或合法性验证。


class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

a = Person('Guido')
print(a.first_name)

# Guido

# a.first_name = 42
# TypeError: Expected a string
a.first_name = "zz"
print(a.first_name)
# zz




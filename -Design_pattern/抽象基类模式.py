# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     抽象基类模式
   Description :
   Author :       jusk?
   date：          2019/11/26
-------------------------------------------------
   Change Activity:
                   2019/11/26:
-------------------------------------------------
"""

# 抽象基类是没法被实例化的。
# 抽象基类中定义抽象方法强制子类去实现，没有实现抽象方法的子类也无法实例化。
# 为了实现这两个特性，我们可以这么写

class Base:
    def foo(self):
        raise NotImplementedError()

    def bar(self):
        raise NotImplementedError()

class Concrete(Base):
    def foo(self):
        return 'foo() called'

    # Oh no, we forgot to override bar()...
    # def bar(self):
    #     return "bar() called"


## python2.6之后的主流写法
from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass
    # We forget to declare bar() again...
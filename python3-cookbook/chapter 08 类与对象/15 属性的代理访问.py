# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     15 属性的代理访问
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# -- 你想将某个实例的属性访问代理到内部另一个实例中去，
# -- 目的可能是作为继承的一个替代方法或者实现代理模式。


# 简单来说，代理是一种编程模式，它将某个操作转移给另外一个对象来实现。
# 最简单的形式可能是像下面这样


class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B1:
    """简单的代理"""

    def __init__(self):
        self._a = A()

    def spam(self, x):
        # Delegate to the internal self._a instance
        return self._a.spam(x)

    def foo(self):
        # Delegate to the internal self._a instance
        return self._a.foo()

    def bar(self):
        pass


class B2:
    """使用__getattr__的代理，代理方法比较多时候"""

    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    # Expose all of the methods defined on class A
    def __getattr__(self, name):
        """这个方法在访问的attribute不存在的时候被调用
        the __getattr__() method is actually a fallback method
        that only gets called when an attribute is not found"""
        return getattr(self._a, name)

# __getattr__ 方法是在访问attribute不存在的时候被调用

b = B1()
b.bar()
b.spam(42)


## 注意__getattr__的使用方法

# https://zhuanlan.zhihu.com/p/67586184
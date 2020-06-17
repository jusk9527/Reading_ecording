# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     07
   Description :
   Author :       jusk?
   date：          2019/12/5
-------------------------------------------------
   Change Activity:
                   2019/12/5:
-------------------------------------------------
"""
# 调用父类方法
# 你想在子类中调用父类的某个已经被覆盖的方法。

class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()  # Call parent spam()

b = B()
print(b.spam())

# B.spam
# A.spam


# super() 函数的一个常见用法是在 __init__() 方法中确保父类被正确的初始化了

# super() 的另外一个常见用法出现在覆盖Python特殊方法的代码中
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value) # Call original __setattr__
        else:
            setattr(self._obj, name, value)

# 在上面代码中，__setattr__() 的实现包含一个名字检查。
# 如果某个属性名以下划线(_)开头，就通过 super() 调用原始的 __setattr__() ，
# 否则的话就委派给内部的代理对象 self._obj 去处理。 这看上去有点意思，
# 因为就算没有显式的指明某个类的父类， super() 仍然可以有效的工作。

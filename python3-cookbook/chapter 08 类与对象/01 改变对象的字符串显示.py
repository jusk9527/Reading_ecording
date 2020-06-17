# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     01
   Description :
   Author :       jusk?
   date：          2019/12/5
-------------------------------------------------
   Change Activity:
                   2019/12/5:
-------------------------------------------------
"""
# -- 你想改变对象实例的打印或显示输出，让它们更具可读性。

## -- 要改变一个实例的字符串表示，可重新定义它的 __str__() 和 __repr__() 方法

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

# __repr__() 方法返回一个实例的代码表示形式，通常用来重新构造这个实例

# __str__() 方法将实例转换为一个字符串，使用 str() 或 print() 函数会输出这个字符串


# >>> p = Pair(3, 4)
# >>> p
# Pair(3, 4) # __repr__() output
# >>> print(p)
# (3, 4) # __str__() output
# >>>


# 我们在这里还演示了在格式化的时候怎样使用不同的字符串表现形式。 特别来讲，!r 格式化代码指明输出使用 __
# repr__() 来代替默认的 __str__() 。 你可以用前面的类来试着测试下：


# >>> p = Pair(3, 4)
# >>> print('p is {0!r}'.format(p))
# p is Pair(3, 4)
# >>> print('p is {0}'.format(p))
# p is (3, 4)
# >>>
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     22 定义上下文管理器的简单方法
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# -- 你想自己去实现一个新的上下文管理器，以便使用with语句。

## -- 实现一个新的上下文管理器的最简单的方法就是使用 contexlib 模块中的 @contextmanager 装饰器。
## -- 下面是一个实现了代码块计时功能的上下文管理器例子


# import time
# from contextlib import contextmanager
#
# @contextmanager
# def timethis(label):
#     start = time.time()
#     try:
#         yield
#     finally:
#         end = time.time()
#         print('{}: {}'.format(label, end - start))
#
# # Example use
# with timethis('counting'):
#     n = 10000000
#     while n > 0:
#         n -= 1


# 在函数 timethis() 中，yield 之前的代码会在上下文管理器中作为 __enter__() 方法执行， 所有在 yield 之后的代码会作为 __exit__() 方法执行



# 如果要写一个上下文管理器，你需要定义一个类，里面包含一个 __enter__() 和一个 __exit__() 方法


class OpenFileDemo(object):
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.f = open(self.filename, 'a+')
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()


with OpenFileDemo('test.txt') as f:
    f.write('Foo\n')




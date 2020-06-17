# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     01
   Description :
   Author :       jusk?
   date：          2019/12/9
-------------------------------------------------
   Change Activity:
                   2019/12/9:
-------------------------------------------------
"""

# 启动与停止线程

import time
# def countdown(n):
#     while n>0:
#         print("T-minus", n)
#         n -=1
#         time.sleep(5)
#
# from threading import Thread
# t = Thread(target=countdown, args=(10,))
# t.start()


# 继承Thread 类实现线程

from threading import Thread

class CountdownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        while self.n > 0:

            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

c = CountdownThread(5)
c.start()


# 由于全局解释锁(GIL)的原因，python 的线程被限制到同一时刻只允许执行这个样一个执行模型
# 所有 python 的线程更适用于处理I/O和其他需要并发执行的阻塞操作(比如等待I/O、等待
# 从数据库获取数据等等),而不是需要多处理并行的计算密集型任务
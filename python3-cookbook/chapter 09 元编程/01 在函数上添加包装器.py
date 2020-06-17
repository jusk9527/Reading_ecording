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


# wraps的作用 https://www.cnblogs.com/Neeo/p/8371826.html
# https://www.cnblogs.com/skaarl/p/9406910.html




# 在函数上添加包装饰器

import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1

rs = countdown(100000)
print(rs)
# countdown 0.008000612258911133

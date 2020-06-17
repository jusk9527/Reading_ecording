# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     02 在创建装饰器时保留函数元信息
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# 你写了一个装饰器作用在某个函数上，但是这个函数的重要的元信息比如名字、
# 文档字符串、注解和参数签名都丢失了。


# 任何时候你定义装饰器的时候，都应该使用 functools 库中的 @wraps 装饰器来注解底层包装函数



import time
from functools import wraps
def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


@timethis
def countdown(n):
    """
    Counts down
    :param n:
    :return:
    """

    while n > 0:
        n -= 1

print(countdown(100000))
# countdown 0.008000612258911133

print(countdown.__name__)
# countdown


print(countdown.__doc__)
# countdown
#
#     Counts down
#     :param n:
#     :return:


print(countdown.__annotations__)
# {}



# 在编写装饰器的时候复制元信息是一个非常重要的部分。如果你忘记了使用 @wraps ，
# 那么你会发现被装饰函数丢失了所有有用的信息


# >>> countdown.__name__
# 'wrapper'
# >>> countdown.__doc__
# >>> countdown.__annotations__
# {}
# >>>
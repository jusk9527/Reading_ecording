# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     03 解除一个装饰器
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""
# 一个装饰器已经作用在一个函数上，你想撤销它，直接访问原始的未包装的那个函数。

# 假设装饰器是通过 @wraps (参考9.2小节)来实现的，
# 那么你可以通过访问 __wrapped__ 属性来访问原始函数：



# --------------------------------------
# 这里的方案仅仅适用于在包装器中正确使用了 @wraps 或者直接设置了 __wrapped__ 属性
# --------------------------------------


from functools import wraps

def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper

@decorator1
@decorator2
def add(x, y):
    return x + y


res = add(2,3)
print(res)

# Decorator 1
# Decorator 2
# 5

res_add = add.__wrapped__(2, 3)
print(res_add)
# Decorator 2
# 5


# 并不是所有的装饰器都使用了 @wraps ，因此这里的方案并不全部适用。
# 特别的，内置的装饰器 @staticmethod 和 @classmethod 就没有遵循这个约定 (它们把原始函数存储在属性 __func__ 中)。

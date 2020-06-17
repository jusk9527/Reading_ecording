# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     装饰器模式
   Description :
   Author :       jusk?
   date：          2019/11/26
-------------------------------------------------
   Change Activity:
                   2019/11/26:
-------------------------------------------------
"""

#
# def fibonacci(n):
#     assert (n >= 0), 'n must be >= 0'
#     return n if n in (0, 1) else fibonacci(n - 1) + fibonacci(n - 2)
#
#
# if __name__ == '__main__':
#     from timeit import Timer
#
#     t = Timer('fibonacci(8)', 'from __main__ import fibonacci')
#     print(t.timeit())
#
# # 12.975208944187468

# 装饰器的话有时候我们在重构和日志添加一些功能的时候有奇效。
# 非常非常的灵活

known = {0:0, 1:1}


def fibonacci(n):
    assert(n >= 0), 'n must be >= 0'
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res


from timeit import Timer
if __name__ == '__main__':
    t = Timer('fibonacci(100)', 'from __main__ import fibonacci')
    print(t.timeit())

# 0.23024004963809444

from functools import wraps

def memoize(fn):
    known = dict()

    @wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]
    return memoizer


@memoize
def fibonacci(n):
    assert(n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    t = Timer('fibonacci(100)', 'from __main__ import fibonacci')
    print(t.timeit())

# 0.27479723724816485
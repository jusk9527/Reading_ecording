# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     14 排序不支持原生比较的对象
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# -- 你想排序类型相同的对象，但是他们不支持原生的比较操作。


## -- 内置的 sorted() 函数有一个关键字参数 key ，可以传入一个 callable 对象给它， 这个 callable 对象对每个传入的对象返回一个值，这个值会被 sorted 用来排序这些对象。 比如，如果你在应用程序里面有一个 User 实例序列，并且你希望通过他们的 user_id 属性进行排序，
## -- 你可以提供一个以 User 实例作为输入并输出对应 user_id 值的 callable 对象。


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))


sort_notcompare()

# [User(23), User(3), User(99)]
# [User(3), User(23), User(99)]





## -- 另外一种方式是使用 operator.attrgetter() 来代替 lambda 函数：

from operator import attrgetter
users = [User(23), User(3), User(99)]
res_attr = sorted(users, key=attrgetter('user_id'))
print(res_attr)
# [User(3), User(23), User(99)]


## -- 适用于同类型的min 和max之类的函数
res_min = min(users, key=attrgetter('user_id'))
print(res_min)
# User(3)

res_max = max(users, key=attrgetter('user_id'))
print(res_max)
# User(99)

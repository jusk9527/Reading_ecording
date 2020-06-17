# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     06 字典中的键映射多个值
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""


# -- 怎样实现一个键对应多个值的字典（也叫 multidict）？

## -- 一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，那么你就需要将这多个值放到另外的容器中，
## -- 比如列表或者集合里面。比如，你可以像下面这样构造这样的字典：


d = {
    'a' : [1, 2, 3],
    'b' : [4, 5]
}

e = {
    'a' : {1, 2, 3},
    'b' : {4, 5}
}


from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)
print(d["a"])

# defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4]})
# [1, 2]



d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

print(d)
print(d["a"])

# defaultdict(<class 'set'>, {'a': {1, 2}, 'b': {4}})
# {1, 2}




# ---------------------------------------------------

# defaultdict 会自动为将要访问的键（就算目前字典中并不存在这样的键）创建映射实体。 如果你并不需要这样的特性，
# 你可以在一个普通的字典上使用 setdefault() 方法来代替。

d = {} # 一个普通的字典
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)

print(d)
print(d["a"])

# {'a': [1, 2], 'b': [4]}
# [1, 2]


# -----------------------------------------------------------
# -- 思考

# d = {}
# for key, value in pairs:
#     if key not in d:
#         d[key] = []
#     d[key].append(value)

# ------------------------------------------------------------
# d = defaultdict(list)
# for key, value in pairs:
#     d[key].append(value)
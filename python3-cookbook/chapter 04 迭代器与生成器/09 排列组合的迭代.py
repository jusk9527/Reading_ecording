# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     09
   Description :
   Author :       jusk?
   date：          2019/12/3
-------------------------------------------------
   Change Activity:
                   2019/12/3:
-------------------------------------------------
"""
# permutations有置换的意思
from itertools import permutations
items = ['a', 'b', 'c']
for p in permutations(items):
    print(p)

# ('a', 'b', 'c')
# ('a', 'c', 'b')
# ('b', 'a', 'c')
# ('b', 'c', 'a')
# ('c', 'a', 'b')
# ('c', 'b', 'a')


# 指定长度
for p in permutations(items, 2):
    print(p)

# ('a', 'b')
# ('a', 'c')
# ('b', 'a')
# ('b', 'c')
# ('c', 'a')
# ('c', 'b')



# 使用 itertools.combinations() 可得到输入集合中元素的所有的组合
# 集合、意味着没有重复
from itertools import combinations
for c in combinations(items, 3):
    print(c)

# ('a', 'b', 'c')


for c in combinations(items, 2):
    print(c)

# ('a', 'b')
# ('a', 'c')
# ('b', 'c')

for c in combinations(items, 1):
    print(c)

# ('a',)
# ('b',)
# ('c',)


# 函数 itertools.combinations_with_replacement() 允许同一个元素被选择多次
from itertools import combinations_with_replacement
for c in combinations_with_replacement(items, 3):
    print(c)

# ('a', 'a', 'a')
# ('a', 'a', 'b')
# ('a', 'a', 'c')
# ('a', 'b', 'b')
# ('a', 'b', 'c')
# ('a', 'c', 'c')
# ('b', 'b', 'b')
# ('b', 'b', 'c')
# ('b', 'c', 'c')
# ('c', 'c', 'c')
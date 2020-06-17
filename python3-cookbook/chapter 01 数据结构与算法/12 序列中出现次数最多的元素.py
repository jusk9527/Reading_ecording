# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     12 序列中出现次数最多的元素
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""
# -- 怎样找出一个序列中出现次数最多的元素呢？

## -- collections.Counter 类就是专门为这类问题而设计的，
## -- 它甚至有一个有用的 most_common() 方法直接给了你答案。

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter
words_count = Counter(words)
top_three = words_count.most_common(3)
print(top_three)
# [('eyes', 8), ('the', 5), ('look', 4)]


print(words_count['not'])
# 1

print(words_count['eyes'])
# 8




## -- 手动的话
morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    words_count[word] += 1

res = words_count["eyes"]
print(res)
# 9



# --------------------------------------------------------------
## - 可以与数学运算符相结合
a = Counter(words)
b = Counter(morewords)
print(a)
# Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2, 'not': 1, "don't": 1, "you're": 1, 'under': 1})
print(b)
# Counter({'why': 1, 'are': 1, 'you': 1, 'not': 1, 'looking': 1, 'in': 1, 'my': 1, 'eyes': 1})

c = a+b
print(c)
# Counter({'eyes': 9, 'the': 5, 'look': 4, 'my': 4, 'into': 3, 'not': 2, 'around': 2, "don't": 1, "you're": 1, 'under': 1, 'why': 1, 'are': 1, 'you': 1, 'looking': 1, 'in': 1})


d = a - b
print(d)
# Counter({'eyes': 7, 'the': 5, 'look': 4, 'into': 3, 'my': 2, 'around': 2, "don't": 1, "you're": 1, 'under': 1})

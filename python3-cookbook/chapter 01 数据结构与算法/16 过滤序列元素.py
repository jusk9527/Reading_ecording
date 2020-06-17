# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     16 过滤序列元素
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# -- 你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列
## -- 最简单的过滤序列元素的方法就是使用列表推导。比如：

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
res_first = [n for n in mylist if n > 0]
print(res_first)
# [1, 4, 10, 2, 3]

res_two = [n for n in mylist if n < 0]
print(res_two)
# [-5, -7, -1]


## -- 列表生成式就是占内存，其他都好，有洁癖的话就使用生成器吧
pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)

# 1
# 4
# 10
# 2
# 3



## -- 最好可以使用filter高阶函数

values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)
# ['1', '2', '-3', '4', '5']


## -- filter() 函数创建了一个迭代器，因此如果你想得到一个列表的话，就得像示例那样使用 list() 去转换。

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math
res_three = [math.sqrt(n) for n in mylist if n > 0]
# print(res_three)[1.0, 2.0, 3.1622776601683795, 1.4142135623730951, 1.7320508075688772]



## -- 另外一个值得关注的过滤工具就是 itertools.compress()
## -- 它以一个 iterable 对象和一个相对应的 Boolean 选择器序列作为输入参数
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

## -- 现在你想将那些对应 count 值大于5的地址全部输出，那么你可以这样做：

from itertools import compress
more5 = [n>5 for n in counts]
print(more5)
# [False, False, True, False, False, True, True, False]

res_com = list(compress(addresses, more5))
print(res_com)
# ['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']

## 和 filter() 函数类似， compress() 也是返回的一个迭代器。因此，如果你需要得到一个列表，
## 那么你需要使用 list() 来将结果转换为列表类型。
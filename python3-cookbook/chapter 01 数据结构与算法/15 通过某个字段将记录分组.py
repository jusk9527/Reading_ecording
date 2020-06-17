# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     15 通过某个字段将记录分组
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# -- 你有一个字典或者实例的序列，然后你想根据某个特定的字段比如 date 来分组迭代访问

## -- itertools.groupby() 函数对于这样的数据分组操作非常实用。
## -- 为了演示，假设你已经有了下列的字典列表



rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]




from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)



# 07/01/2012
#   {'address': '5412 N CLARK', 'date': '07/01/2012'}
#   {'address': '4801 N BROADWAY', 'date': '07/01/2012'}
# 07/02/2012
#   {'address': '5800 E 58TH', 'date': '07/02/2012'}
#   {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}
#   {'address': '1060 W ADDISON', 'date': '07/02/2012'}
# 07/03/2012
#   {'address': '2122 N CLARK', 'date': '07/03/2012'}
# 07/04/2012
#   {'address': '5148 N CLARK', 'date': '07/04/2012'}
#   {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}


## groupby() 函数扫描整个序列并且查找连续相同值（或者根据指定 key 函数返回值相同）
## 的元素序列。 在每次迭代的时候，它会返回一个值和一个迭代器对象， 这个迭代器对象可以生成元素值全部等于上面那个值的组中所有对象。
## 一个非常重要的准备步骤是要根据指定的字段将数据排序。 因为 groupby() 仅仅检查连续的元素，如果事先并没有排序完成的话，
## 分组函数将得不到想要的结果
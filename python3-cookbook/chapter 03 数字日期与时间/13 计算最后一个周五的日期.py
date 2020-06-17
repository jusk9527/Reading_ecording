# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     计算最后一个周五的日期
   Description :
   Author :       jusk?
   date：          2019/12/2
-------------------------------------------------
   Change Activity:
                   2019/12/2:
-------------------------------------------------
"""

# 计算最后一个周五的日期

from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

print(datetime.today())
# 2019-12-02 14:58:51.244632

print(get_previous_byday('Monday'))
# 2019-11-25 14:59:23.517478

print(get_previous_byday('Tuesday'))
# 2019-11-26 15:00:52.082544

print(get_previous_byday('Friday'))
# 2019-11-29 15:01:10.066572


print(get_previous_byday('Sunday', datetime(2019, 12, 21)))
# 2019-12-15 00:00:00


## 上面的算法原理是这样的：
## 先将开始日期和目标日期映射到星期数组的位置上(星期一索引为0)，
## 然后通过模运算计算出目标日期要经过多少天才能到达开始日期。
## 然后用开始日期减去那个时间差即得到结果日期。
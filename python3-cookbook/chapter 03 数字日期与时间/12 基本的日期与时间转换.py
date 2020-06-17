# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     12
   Description :
   Author :       jusk?
   date：          2019/12/2
-------------------------------------------------
   Change Activity:
                   2019/12/2:
-------------------------------------------------
"""

# 基本的日期与时间转换

from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c= a+b
print(c.days)
# 2
print(c.seconds)
# 37800
print(c.seconds/3600)
# 10.5
print(c.total_seconds()/3600)
# 58.5

from datetime import datetime
a = datetime(2012,9,23)
print(a+timedelta(days=10))
# 2012-10-03 00:00:00
b = datetime(2012, 12, 21)
d = b - a
print(d.days)
# 89

now = datetime.today()
print(now)
# 2019-12-02 14:50:27.573824
print(now + timedelta(minutes=10))
# 2019-12-02 15:01:08.040139



# 计算闰年
a = datetime(2012, 3,1)
b = datetime(2012, 2, 28)
c = a-b
print(c.days)

# 2

c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)

print((c-d).days)
# 1
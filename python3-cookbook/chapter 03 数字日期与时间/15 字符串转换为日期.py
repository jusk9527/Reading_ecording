# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     15
   Description :
   Author :       jusk?
   date：          2019/12/2
-------------------------------------------------
   Change Activity:
                   2019/12/2:
-------------------------------------------------
"""
# 字符串转换为日期
from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
print(y)
# 2012-09-20 00:00:00

diff = z -y
print(diff.days)
# 2629
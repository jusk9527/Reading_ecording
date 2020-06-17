# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     05
   Description :
   Author :       jusk?
   date：          2019/12/2
-------------------------------------------------
   Change Activity:
                   2019/12/2:
-------------------------------------------------
"""

# 字符串搜索和替换

text = "yeah, but no, but yeah, but no, but yeah"
res = text.replace("yeah", 'yep')
print(res)
# yep, but no, but yep, but no, but yep

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
res = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(res)
# Today is 2012-11-27. PyCon starts 2013-3-13.

## sub() 函数中的第一个参数是被匹配的模式，第二个参数是替换模式。反斜杠数字比如 \3 指向前面模式的捕获组号。


import re
datapat = re.compile(r'(\d+)/(\d+)/(\d+)')
res = datapat.sub(r'\3-\1-\2', text)
print(res)
# Today is 2012-11-27. PyCon starts 2013-3-13.


from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

res  = datapat.sub(change_date, text)
print(res)
# Today is 27 Nov 2012. PyCon starts 13 Mar 2013.
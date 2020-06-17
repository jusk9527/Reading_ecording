# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     01
   Description :
   Author :       jusk?
   date：          2019/12/2
-------------------------------------------------
   Change Activity:
                   2019/12/2:
-------------------------------------------------
"""
import re
# 使用多个界定符分割字符串
"""
string 对象的split()方法只适合非常简单的字符串分割情形
他并不语序有多个分隔符或者是分隔符周围不确定的空格
当你需要更加灵活的切割字符串的时候，最后使用re.split()方法
"""
line = 'asdf fjdk; afed, fjek,asdf, foo'

res = re.split(r'[;,\s]\s*', line)
print(res)

# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']


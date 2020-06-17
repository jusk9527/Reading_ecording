# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     07
   Description :
   Author :       jusk?
   date：          2019/12/2
-------------------------------------------------
   Change Activity:
                   2019/12/2:
-------------------------------------------------
"""
# 最短匹配模式
import re
str_pat = re.compile(r'"(.*)"')
text1 = 'Computer says "no."'

res = str_pat.findall(text1)
print(res)

# ['no.']

text2 = 'Computer says "no." Phone says "yes."'
res = str_pat.findall(text2)
print(res)

# ['no." Phone says "yes.']


str_pat = re.compile(r'"(.*?)"')
res = str_pat.findall(text2)
print(res)

# ['no.', 'yes.']
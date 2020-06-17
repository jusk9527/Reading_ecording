# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     04
   Description :
   Author :       jusk?
   date：          2019/12/2
-------------------------------------------------
   Change Activity:
                   2019/12/2:
-------------------------------------------------
"""

# 字符串匹配和搜索

text = 'yeah, but no, but yeah, but no, but yeah'
print(text == "yeah")
# False
res = text.startswith("yeah")
print(res)
# True

res = text.endswith('no')
print(res)
# False


# 查找第一次查询的下标
res = text.find('no')
print(res)


text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re
if re.match(r'\d+/\d+/\d+', text1):
    print("yes")
else:
    print("no")

# yes


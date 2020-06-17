# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     03
   Description :
   Author :       jusk?
   date：          2019/12/2
-------------------------------------------------
   Change Activity:
                   2019/12/2:
-------------------------------------------------
"""

# -- 你需要将数字格式化后输出，并控制数字的位数、对齐、千位分隔符和其他的细节。


## -- 格式化输出单个数字的时候，可以使用内置的 format() 函数

x = 1234.56789

rs = format(x, '0.2f')
print(rs)

# 1234.57

# Right justified in 10 chars, one-digit accuracy
rs = format(x, '>10.1f')
print(rs)

#     1234.6

# Left justified
rs = format(x, '<10.1f')
print(rs)
# 1234.6     '
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

# -- 你需要转换或者输出使用二进制，八进制或十六进制表示的整数。

## -- 为了将整数转换为二进制、八进制或十六进制的文本串

x = 1234
rs = bin(x)
print(rs)
# 0b10011010010
rs = oct(x)
print(rs)
# 0o2322
rs = hex(x)
print(rs)
# 0x4d2





rs = format(x,'b')
print(rs)
# 10011010010

rs = format(x, 'o')
print(rs)
# 2322

rs = format(x, 'x')
print(rs)
# 4d2




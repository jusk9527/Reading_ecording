# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     07
   Description :
   Author :       jusk?
   date：          2019/12/5
-------------------------------------------------
   Change Activity:
                   2019/12/5:
-------------------------------------------------
"""

# 匿名函数捕获变量值
## 你用lambda定义了一个匿名函数，并想在定义时捕获到某些变量的值。

x = 10
a = lambda y:x+y
x = 20
b = lambda y:x+y

rs = a(10)
print(rs)
# 30

rs = b(10)
print(rs)
# 30

funcs = [lambda x: x+n for n in range(3)]
for f in funcs:
    print(f(0))

# 2
# 2
# 2
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     02
   Description :
   Author :       jusk?
   date：          2019/12/2
-------------------------------------------------
   Change Activity:
                   2019/12/2:
-------------------------------------------------
"""

# -- 你需要对浮点数执行精确的计算操作，并且不希望有任何小误差的出现。


## 浮点数的一个普遍问题是它们并不能精确的表示十进制数。
## 并且，即使是最简单的数学运算也会产生小的误差，
from decimal import Decimal

a = Decimal('4.2')
b = Decimal('2.1')
res = a+b
print(res)
# 6.3

print((a + b) == Decimal('6.3'))
# True

from decimal import localcontext
a = Decimal("1.3")
b = Decimal('1.7')
print(a/b)
# 0.7647058823529411764705882353

with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)

# 0.765

with localcontext() as ctx:
    ctx.prec = 50
    print(a/b)

# 0.76470588235294117647058823529411764705882352941176
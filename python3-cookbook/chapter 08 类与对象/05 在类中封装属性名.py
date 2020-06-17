# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     05
   Description :
   Author :       jusk?
   date：          2019/12/5
-------------------------------------------------
   Change Activity:
                   2019/12/5:
-------------------------------------------------
"""

# -- 你想封装类的实例上面的“私有”数据，但是Python语言并没有访问控制。

## -- Python程序员不去依赖语言特性去封装数据，而是通过遵循一定的属性和方法命名规约来达到这个效果。
## -- 第一个约定是任何以单下划线_开头的名字都应该是内部实现

class A():
    def __init__(self,a,b,c):
        self.__a = a
        self._b = b
        self.c = c

    def visit(self):
        m = self.__a
        return m

rs = A(1,2,3)
# print(rs.__a)
# AttributeError: 'A' object has no attribute '__a'


print(rs._b)
# 2
print(rs.c)
# 3


# 访问__a只能内部访问

print(rs.visit())
# 1

# 更多的 "_a"这种模式是防止重名
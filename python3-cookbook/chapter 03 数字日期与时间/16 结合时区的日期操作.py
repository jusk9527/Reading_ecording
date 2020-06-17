# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     16
   Description :
   Author :       jusk?
   date：          2019/12/2
-------------------------------------------------
   Change Activity:
                   2019/12/2:
-------------------------------------------------
"""


# 结合时区的日期操作

from datetime import datetime

def createGenerator() :
    mylist = range(3)
    for i in mylist :
         yield i*i

mygenerator = createGenerator()
print(mygenerator)

for i in mygenerator:
    print(i)


# <generator object createGenerator at 0x00000000024BCF10>
# 0
# 1
# 4
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     13
   Description :
   Author :       jusk?
   date：          2019/12/4
-------------------------------------------------
   Change Activity:
                   2019/12/4:
-------------------------------------------------
"""

class B:
    def __init__(self):
        self.private = 0

    @property
    def private1(self):
        return self.private


b = B()
print(b.private1)
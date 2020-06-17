# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :       jusk?
   date：          2019/12/5
-------------------------------------------------
   Change Activity:
                   2019/12/5:
-------------------------------------------------
"""

class User():
    def __init__(self,name,age):
        self.name = "dd"
        self.age = "c"

    def __get__(self, instance, owner):
        print("dd")

    def __set__(self, instance, value):
        print("dz")

class C():
    def __init__(self):
       pass

    user = User("xiao",13)
c = C()
c.user
c.user = "xiah"

# dd
# dz


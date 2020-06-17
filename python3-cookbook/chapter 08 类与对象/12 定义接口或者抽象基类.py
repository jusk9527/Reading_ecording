# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     12
   Description :
   Author :       jusk?
   date：          2019/12/5
-------------------------------------------------
   Change Activity:
                   2019/12/5:
-------------------------------------------------
"""

# 定义接口或者抽象基类
# 你想定义一个接口或抽象类，并且通过执行类型检查来确保子类实现了某些特定的方法

from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass
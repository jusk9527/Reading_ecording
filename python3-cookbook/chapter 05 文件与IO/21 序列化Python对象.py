# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     21
   Description :
   Author :       jusk?
   date：          2019/12/3
-------------------------------------------------
   Change Activity:
                   2019/12/3:
-------------------------------------------------
"""
# 序列化Python对象


## 你需要将一个Python对象序列化为一个字节流，
## 以便将它保存到一个文件、存储到数据库或者通过网络传输它。


import pickle

data = ... # Some Python object
f = open('somefile', 'wb')
pickle.dump(data, f)
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

# 字符串开头或结尾匹配

filename = 'spam.txt'
res = filename.endswith('.txt')
print(res)
# True
res = filename.startswith('file:')
print(res)
# False
url = "http://www.python.org"
res = url.startswith("http:")
print(res)
# True


# 确保传参先调用tuple()将其转换为元组类型

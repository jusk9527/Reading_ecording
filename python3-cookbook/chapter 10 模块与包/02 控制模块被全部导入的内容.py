# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     02
   Description :
   Author :       jusk?
   date：          2019/12/5
-------------------------------------------------
   Change Activity:
                   2019/12/5:
-------------------------------------------------
"""

#  控制模块被全部导入的内容

# somemodule.py
def spam():
    pass

def grok():
    pass

blah = 42
# Only export 'spam' and 'grok'
__all__ = ['spam', 'grok']
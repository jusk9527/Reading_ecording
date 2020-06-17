# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     03
   Description :
   Author :       jusk?
   date：          2019/12/5
-------------------------------------------------
   Change Activity:
                   2019/12/5:
-------------------------------------------------
"""
# 使用相对路径名导入包中子模块
## 将代码组织成包,想用import语句从另一个包名没有硬编码过的包中导入子模块。

# mypackage/
#     __init__.py
#     A/
#         __init__.py
#         spam.py
#         grok.py
#     B/
#         __init__.py
#         bar.py


# mypackage/A/spam.py
# from . import grok

# mypackage/A/spam.py
# from ..B import bar


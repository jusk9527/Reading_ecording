# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     01
   Description :
   Author :       jusk?
   date：          2019/12/5
-------------------------------------------------
   Change Activity:
                   2019/12/5:
-------------------------------------------------
"""
# 构建一个模块的层级包

## 你想将你的代码组织成由很多分层模块构成的包。


# graphics/
#     __init__.py
#     primitive/
#         __init__.py
#         line.py
#         fill.py
#         text.py
#     formats/
#         __init__.py
#         png.py
#         jpg.py


# 导入就很方便了
# import graphics.primitive.line
# from graphics.primitive import line
# import graphics.formats.jpg as jpg
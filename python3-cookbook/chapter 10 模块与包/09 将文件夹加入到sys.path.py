# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     09
   Description :
   Author :       jusk?
   date：          2019/12/5
-------------------------------------------------
   Change Activity:
                   2019/12/5:
-------------------------------------------------
"""

import sys


# 将文件夹加入到sys.path
"""
你无法导入你的Python代码因为它所在的目录不在sys.path里。
你想将添加新目录到Python路径，但是不想硬链接到你的代码。
"""
rs = sys.path
print(rs)


from os.path import abspath, join, dirname
sys.path.insert(0, join(abspath(dirname(__file__)), 'src'))
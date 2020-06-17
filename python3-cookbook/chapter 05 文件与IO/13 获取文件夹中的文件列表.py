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

# 获取文件夹中的文件列表
import os
names = os.listdir("python3-cookbook/chapter 02 字符串与文本")
print(names)

['01 使用多个界定符分割字符串.py', '02 字符串开头或结尾匹配.py', '03 用Shell通配符匹配字符串.py', '04 字符串匹配和搜索.py', '05 字符串搜索和替换.py', '06 字符串忽略大小写的搜索替换.py', '07 最短匹配模式.py', '11 删除字符串中不需要的字符.py', '12 审查清理文本字符串.py']

import os.path

# Get all regular files
names = [name for name in os.listdir('somedir')
        if os.path.isfile(os.path.join('somedir', name))]

# Get all dirs
dirnames = [name for name in os.listdir('somedir')
        if os.path.isdir(os.path.join('somedir', name))]

pyfiles = [name for name in os.listdir('somedir')
            if name.endswith('.py')]


import glob
pyfiles = glob.glob('somedir/*.py')

from fnmatch import fnmatch
pyfiles = [name for name in os.listdir('somedir')
            if fnmatch(name, '*.py')]



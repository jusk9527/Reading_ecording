# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     12
   Description :
   Author :       jusk?
   date：          2019/12/4
-------------------------------------------------
   Change Activity:
                   2019/12/4:
-------------------------------------------------
"""

# 测试文件是否存在

import os
rs = os.path.exists('/etc/passwd')
print(rs)
# False


## Is a regular file
rs = os.path.isfile('/etc/passwd')
print(rs)
# False

## Is a symbolic link
rs = os.path.islink('/usr/local/bin/python3')
print(rs)
# False
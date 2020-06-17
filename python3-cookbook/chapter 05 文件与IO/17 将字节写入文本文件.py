# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     17
   Description :
   Author :       jusk?
   date：          2019/12/5
-------------------------------------------------
   Change Activity:
                   2019/12/5:
-------------------------------------------------
"""
# 将字节写入文本文件

## 你想在文本模式打开的文件中写入原始的字节数据。

import sys
sys.stdout.write(b'Hello\n')

# Traceback (most recent call last):
#   File "C:/Users/Administrator/Desktop/准备/python3-cookbook/chapter 05 文件与IO/17 将字节写入文本文件.py", line 18, in <module>
#     sys.stdout.write(b'Hello\n')
# TypeError: write() argument must be str, not bytes

# 将字节数据直接写入文件的缓冲区即可，例如：
res = sys.stdout.buffer.write(b'Hello\n')
print(res)

# Hello
# 6
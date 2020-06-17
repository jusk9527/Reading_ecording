# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     07
   Description :
   Author :       jusk?
   date：          2019/12/4
-------------------------------------------------
   Change Activity:
                   2019/12/4:
-------------------------------------------------
"""

# 读写压缩文件

# gzip compression
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

# bz2 compression
import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()


# gzip compression
import gzip
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

# bz2 compression
import bz2
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)


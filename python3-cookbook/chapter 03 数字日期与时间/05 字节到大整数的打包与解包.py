# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     05 字节到大整数的打包与解包
   Description :
   Author :       jusk?
   date：          2019/12/30
-------------------------------------------------
   Change Activity:
                   2019/12/30:
-------------------------------------------------
"""

# -- 你有一个字节字符串并想将它解压成一个整数。或者，
# -- 你需要将一个大整数转换为一个字节字符串



## -- 假设你的程序需要处理一个拥有128位长的16个元素的字节字符串

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

res_len = len(data)


## -- 为了将bytes解析为整数，使用 int.from_bytes() 方法
print(res_len)
# 16

res_int_first = int.from_bytes(data, 'little')
print(res_int_first)
# 69120565665751139577663547927094891008
res_int_two = int.from_bytes(data, 'big')
print(res_int_two)
# 94522842520747284487117727783387188
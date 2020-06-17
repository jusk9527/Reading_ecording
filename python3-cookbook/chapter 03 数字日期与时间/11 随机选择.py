# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     11
   Description :
   Author :       jusk?
   date：          2019/12/3
-------------------------------------------------
   Change Activity:
                   2019/12/3:
-------------------------------------------------
"""
# 随机选择


import random

values = [1,2,3,4,5,6]
rs = random.choice(values)
print(rs)
# 5


# 随机选择固定长度的不同元素
rs = random.sample(values,2)
print(rs)
# [6, 4]

# 打乱元素顺序

random.shuffle(values)
print(values)
# [4, 2, 6, 1, 3, 5]

# 生成随机整数
rs = random.randint(0,10)
print(rs)
# 8

# 生成0到1的均与分布的浮点数
rs = random.random()
print(rs)
# 0.6773483859182466


# 获取N位随机位(二进制)的整数
rs = random.getrandbits(3)
print(rs)
# 4


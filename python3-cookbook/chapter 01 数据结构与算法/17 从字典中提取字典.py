# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     17 从字典中提取字典
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# -- 你想构造一个字典，它是另外一个字典的子集。


prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# Make a dictionary of all prices over 200
p1 = {key: value for key, value in prices.items() if value > 200}
# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}


print(p1)
# {'AAPL': 612.78, 'IBM': 205.55}
print(p2)
# {'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.2}




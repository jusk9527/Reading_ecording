# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     20 合并多个字典映射
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# -- 现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某些操作，
# -- 比如查找值或者检查某些键是否存在。

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }


from collections import ChainMap
c = ChainMap(a,b)
print(c['x'])
print(c['y'])
print(c['z'])



# 1
# 2
# 3

# 如果出现重复键，那么第一次出现的映射值会被返回。 因此，例子程序中的 c['z'] 总是会返回字典 a 中对应的值，而不是 b 中对应的值。


values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
# ChainMap({'x': 3}, {'x': 2}, {'x': 1})



## -- 作为 ChainMap 的替代，你可能会考虑使用 update() 方法将两个字典合并。比如：
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
merged = dict(b)
merged.update(a)
print(merged)
# {'y': 2, 'z': 3, 'x': 1}

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4}
merged = ChainMap(a,b)
print(merged)
# ChainMap({'x': 1, 'z': 3}, {'y': 2, 'z': 4})


## -- ChainMap 使用原来的字典，它自己不创建新的字典。所以它并不会产生上面所说的结果
a['x'] = 42
print(merged['x'])

# 42


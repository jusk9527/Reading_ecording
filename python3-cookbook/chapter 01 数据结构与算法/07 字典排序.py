# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     07 字典排序
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""
# -- 你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。

## -- 为了能控制一个字典中元素的顺序，你可以使用 collections 模块中的 OrderedDict 类。
## -- 在迭代操作的时候它会保持元素被插入时的顺序，示例如下：


from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])

# foo 1
# bar 2
# spam 3
# grok 4



# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     01
   Description :
   Author :       jusk?
   date：          2019/12/4
-------------------------------------------------
   Change Activity:
                   2019/12/4:
-------------------------------------------------
"""

# 可接受任意数量参数的函数

## 你想构造一个可接受任意数量参数的函数。

def avg(first, *rest):
    print(rest)
    return (first + sum(rest)) / (1 + len(rest))

# Sample use
rs = avg(1, 2) # 1.5
print(rs)
rs = avg(1, 2, 3, 4) # 2.5
print(rs)


# (2,)
# 1.5
# (2, 3, 4)
# 2.5


## 为了接受任意数量的关键字参数，使用一个以**开头的参数。比如：


import html

def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
                name=name,
                attrs=attr_str,
                value=html.escape(value))
    return element

# Example
# Creates '<item size="large" quantity="6">Albatross</item>'
make_element('item', 'Albatross', size='large', quantity=6)

# Creates '<p>&lt;spam&gt;</p>'
rs = make_element('p', '<spam>')
print(rs)


# <p>&lt;spam&gt;</p>


def anyargs(*args, **kwargs):
    print(args) # A tuple
    print(kwargs) # A dict
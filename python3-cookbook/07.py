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

# 可接受任意数量参数的函数

def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

rs = avg(1, 2)
print(rs)
# 1.5

rs = avg(1, 2, 3, 4)
print(rs)

# 2.5



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
make_element('p', '<spam>')

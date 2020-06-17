# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     将字典转换为XML
   Description :
   Author :       jusk?
   date：          2019/12/26
-------------------------------------------------
   Change Activity:
                   2019/12/26:
-------------------------------------------------
"""

# -- 你想使用一个Python字典存储数据，并将它转换成XML格式

## -- 尽管 xml.etree.ElementTree 库通常用来做解析工作，其实它也可以创建XML文档

from xml.etree.ElementTree import Element

s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


e = dict_to_xml('stock', s)
print(e)
# <Element 'stock' at 0x00000000020CD458>

## -- 转换结果是一个 Element 实例。对于I/O操作，
## -- 使用 xml.etree.ElementTree 中的 tostring() 函数很容易就能将它转换成一个字节字符串。例如：

from xml.etree.ElementTree import tostring
print(tostring(e))
# b'<stock><name>GOOG</name><shares>100</shares><price>490.1</price></stock>'


## -- 如果你想给某个元素添加属性值
e.set('_id','1234')
print(tostring(e))
# b'<stock _id="1234"><name>GOOG</name><shares>100</shares><price>490.1</price></stock>'


# 如果你还想保持元素的顺序，可以考虑构造一个 OrderedDict 来代替一个普通的字典。请参考1.7小节。

# https://python3-cookbook.readthedocs.io/zh_CN/latest/c06/p05_turning_dictionary_into_xml.html
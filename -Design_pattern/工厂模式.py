# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     工厂模式
   Description :
   Author :       jusk?
   date：          2019/11/26
-------------------------------------------------
   Change Activity:
                   2019/11/26:
-------------------------------------------------
"""

# 工厂方法
# 比如我们要一台小米9手机，我们去买，工厂就直接给你一台小米9手机
# 就好比非常规整的工厂一样，你要什么我给你造一台机器




# 下面就是我们有个需求，我们需要解析某个文件的内容，但是我们不知道他的格式是什么
# 这个时候工厂方法就可以很方便解决这个问题，定义一个工厂方法，我们只需要将文件的路径放进入，
# 这个时候就自动解析出内容
import json
import xml.etree.ElementTree as etree

class JSONConnector:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    """ 工厂方法 """
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)
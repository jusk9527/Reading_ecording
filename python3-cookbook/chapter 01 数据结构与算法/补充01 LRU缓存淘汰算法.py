# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     补充01 LRU缓存淘汰算法
   Description :
   Author :       jusk?
   date：          2019/12/31
-------------------------------------------------
   Change Activity:
                   2019/12/31:
-------------------------------------------------
"""

"""
LRU缓存淘汰算法的原理就是：
    1.替换掉最近最少使用的对象
    2.设置的如果在的话就替换，不在就删除前面的，在末尾换上新的
    3.获取的如果在的话取出并将数据放在最后，没有就返回-1

    实现后面的都是使用或者查看最频繁的。替换前面不经常使用的
"""

from collections import OrderedDict
class LRUCache():
    def __init__(self,capacity):
        self.od = OrderedDict()
        # 容量
        self.capacity = capacity

    def get(self,key):
        if key in self.od:
            val = self.od[key]
            self.od.move_to_end(key)
            return val
        else:
            return -1

    def put(self, key, value):
            if key in self.od:
                del self.od[key]
                self.od[key]=value
            else:
                if len(self.od)>=self.capacity:
                    # 如果满了,就把开头的一个删掉
                    self.od.popitem(last=False)
                    self.od[key] = value
                else:
                    self.od[key] = value

cache = LRUCache(capacity=3)

cache.put("1",1)
cache.put("2",2)
cache.put("3",3)
cache.put("4",4)
cache.put("5",5)

cache.get("4")
print(cache.od)

# OrderedDict([('3', 3), ('5', 5), ('4', 4)])
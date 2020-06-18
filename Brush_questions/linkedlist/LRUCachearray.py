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
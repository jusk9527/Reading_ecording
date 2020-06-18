class DblistNode(object):
    def __int__(self,x,y):
        self.key = x
        self.val = y
        self.next = None
        self.prev = None


class LRUCache:
    """
    leet code:1246
    运用你所掌握的数据结构，设计和实现一个LRU(最近最少使用)缓存机制
    他应该支持以下操作：获取数据get 和写入数据put
    获取数据get(key) - 如果秘钥(key)粗只能在与缓存中，则获取秘钥的值(总是正数)，否则返回-1

    获取数据 get(key )----如果秘钥（key） 存在缓存中，则获取秘钥的值（正是正数），否则返回-1

    写入数据 put(key, value)  -- 如果秘钥不存在，则写入其数据值
            当缓存容量达到上限时，他应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值流出空间


    哈希表+双向链表

    哈希表： 查询O(1)
    双向链表：有序，增删操作O(1)
    """
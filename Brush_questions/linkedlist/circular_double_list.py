# Node节点，表示每一个元素
class Node(object):
    # 定义节点，两个值：value，prew, next
    def __init__(self, value=None, prew=None, next=None):
        self.value, self.prew, self.next = value, prew, next


# 循环双端链表
class CircualDoubleLinedList(object):
    # 初始化

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prew = node,node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    # 头节点
    def headnode(self):
        return self.root.next

    # 最后节点
    def tailnode(self):
        return self.root.prew

    # 添加操作
    def append(self, value):
        # 判断是否超过了最大值，若超过了，抛出异常
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('FUll')

        node = Node(value=value)
        tailnode = self.tailnode
        tailnode.next = node
        node.prew = tailnode
        node.next = self.root
        self.root.prew = node
        self.length += 1

    # 左侧插入
    def appendleft(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('FUll')
        node = Node(value=value)
        # 如果节点为空
        if self.root.next is self.root:
            node.next = self.root
            node.prew = self.root
            self.root.next = node
            self.root.prew = node
        else:
            node.prew = self.root
            headnode = self.root.next
            node.next = headnode
            headnode.prew = node
            self.root.next = node
        self.length += 1

    # 删除操作，O(1)
    def remove(self, node):
        if node is self.root:
            return
        else:
            node.prew.next = node.next
            node.next.prew = node.prew
        self.length -= 1
        return node

    # 遍历
    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode

    # __iter__方法
    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    # 反向遍历
    def iter_node_reverse(self):
        if self.root.prew is self.root:
            return
        curnode = self.root.prew
        while curnode.prew is not self.root:
            yield curnode
            curnode = curnode.prew
        yield curnode


    def print_all(self):
        """
        打印当前链表所有节点数据
        :return:
        """
        pos = self.root
        if pos is None:
            print("当前链表还没有数据")
            return

        list = []
        while pos.next is not None and pos.next != self.root:
            list.append(pos.data)
            print(str(pos.data) + "--->", end="")
            pos = pos.next_node

        print(str(pos.data))
        list.append(pos.data)
        return list

# 测试
def test_double_link_list():
    dll = CircualDoubleLinedList()
    assert len(dll) == 0

    dll.append(0)
    dll.append(1)
    dll.append(2)

    assert list(dll) == [0, 1, 2]

    assert [node.value for node in dll.iter_node()] == [0, 1, 2]
    assert [node.value for node in dll.iter_node_reverse()] == [2, 1, 0]

    headnode = dll.headnode()
    assert headnode.value == 0

    dll.remove(headnode)
    assert len(dll) == 2
    assert [node.value for node in dll.iter_node()] == [1, 2]

    dll.appendleft(0)
    assert [node.value for node in dll.iter_node_reverse()] == [2, 1, 0]


test_double_link_list()
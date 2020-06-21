class Node(object):
    """
    双链表
    """
    def __init__(self, data):
        """
        双链表节点
        :param data:
        """
        self.data = data
        self.pre = None
        self.next = None


class DoubleLinkedList(object):
    """
    双链表
    """
    def __init__(self, node=None):
        self.__head = node


    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        return self.__head  is None

    def length_by_node(self):
        """
        获取链表长度
        :return:
        """
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count


    def add_head_by_node(self, elem):
        """
        向双链表头部添加元素
        :param elem:
        :return:
        """
        node = Node(elem)
        if self.is_empty():     # 链表为空
            self.__head = node
        else:
            node.next = self.__head
            # node.next.pre = node          # 同样可以这样写
            self.__head.pre = node
            self.__head = node




    def append_last_by_node(self, elem):
        """
        向链表尾部添加节点
        :param elem:
        :return:
        """
        node = Node(elem)
        if  self.is_empty():
            self.__head = node

        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next

            cur.next = node
            node.pre = cur

        return node


    def insert_before(self, node, value):
        """
        在某个节点之前 处插入元素elem
        :param pos:
        :param elem:
        :return:
        """
        if (node is None) or (self.__head is None):
            return

        # 插入到头节点
        if node == self.__head:
            self.add_head_by_node(value)
            return

        new_node = Node(value)

        # 前一个节点
        pre = self.__head

        # 当前节点
        node = self.__head.next
        not_fount = False
        while pre.next != node:
            if pre.next is None:
                not_fount = True
                break
            else:
                pre = node
                node = node.next

        if not not_fount:
            pre.next = new_node

            new_node.pre = pre

            new_node.next = node

            node.pre = new_node.next










    def remove_by_node(self,value):
        """
        删除链表中第一个值为elem的节点
        :param self:
        :param elem:
        :return:
        """
        if self.is_empty():
            return

        if self.__head.data == value:        # 如果链表的头Node节点就是指定删除的Node节点
            self.__head = self.__head.next


        # 前一个节点
        pre = self.__head

        # 当前节点
        node = self.__head.next

        not_found = False
        while node.data != value:
            if node.next is None:      # 如果已经到链表的最后一个节点，则表明该链表中没有找到执行value值的Node节点
                not_found = True
                break
            else:
                pre = node
                node = node.next

        if not_found is False:
            pre.next = node.next
            node.next.pre = pre.next








    def search_by_node(self, elem):
        """
        查找链表中是否有元素elem
        :param elem:
        :return:
        """
        cur = self.__head
        while cur is not None:
            if cur.data == elem:
                return True

            else:
                cur = cur.next

        return False


    def print_all(self):
        """
        打印当前链表所有节点数据
        :return:
        """
        pos = self.__head
        if pos is None:
            print("当前链表还没有数据")
            return

        list = []
        while pos.next is not None:
            list.append(pos.data)
            print(str(pos.data) + "--->", end="")
            pos = pos.next

        print(str(pos.data))
        list.append(pos.data)
        return list



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

    def travel_by_node(self):
        """
        遍历链表
        :return:
        """
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=' ')
            cur = cur.next

        print()

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


    def insert_before(self, pos, elem):
        """
        向链表位置pos 处插入元素elem
        :param pos:
        :param elem:
        :return:
        """
        # 插入到头节点
        if pos <= 0:
            self.add_head_by_node(elem)

        # 插入到最后
        elif pos > (self.length_by_node() - 1):
            self.append_last_by_node(elem)

        else:
            cur = self.__head
            count = 0
            while count < pos:
                cur = cur.next
                count +=1


            # 退出循环时，cur即为pos位置
            node = Node(elem)

            node.next = cur
            cur.pre.next = node
            cur.pre = node













    def remove_by_node(self,data):
        """
        删除链表中第一个值为elem的节点
        :param self:
        :param elem:
        :return:
        """
        if self.is_empty():
            return

        cur = self.__head
        while cur.next != self.__head:
            if cur.data == data:
                if cur == self.__head:          # 如果是头节点
                    self.__head = cur.next      # 链表中只有一个节点
                    if cur.next:
                        cur.next.pre = None

                else:
                    cur.pre.next = cur.next
                    if cur.next:        # 如果不是尾节点
                        cur.next.pre = cur.pre
                break
            else:
                cur = cur.next

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



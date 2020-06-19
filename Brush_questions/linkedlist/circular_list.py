from Brush_questions.linkedlist.singlyLinkedList import Node

class CircularList():
    """
    单向循环链表
    """

    def __init__(self,head=None):
        """
        单向列表的初始化方法===头节点
        """
        self.__head = head

    @property
    def head(self):
        return self.__head


    @head.setter
    def head(self, head):
        self.__head = head

    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        if self.__head == None:
            return True
        else:
            return False

    def find_by_value(self, value):
        """
        按照数据值在单向列表中查找
        :param value: 查找的数据
        :return:Node
        """
        node = self.__head
        while (node is not None) and (node.data != value) and (self.__head != node.next_node):
            node = node.next_node
        return node


    def find_by_index(self, index):
        """
        按照索引值在列表中查找
        :param index: 索引值
        :return: Node
        """
        node = self.__head
        pos = 0
        while (node is not None) and (pos != index) and (self.__head != node.next_node):
            node = node.next_node
            pos += 1
        return node

    def insert_to_head(self, value):
        """
        在链表的头部插入一个存储value数值的Node节点
        :param value:将要存储的数据
        :return:
        """
        node = Node(value)
        last_node = self.find_last_node()

        node.next_node = self.__head
        self.__head = node

        # 最后节点从新指向头节点

        last_node.next_node = node
        return node


    def insert_after(self, node, value):
        """
        在链表的某个指定Node节点之后插入一个存储value数据的Node节点
        :param node:指定的一个Node节点
        :param value:将要存储在新的Node节点中的数据
        :return:
        """
        if node is None:        # 如果指定在一个空节点之后插入数据节点，则什么都不做
            return

        new_node = Node(value)
        new_node.next_node = node.next_node
        node.next_node = new_node

        return new_node

    def insert_before(self, node, value):
        if (node is None) or (self.__head is None):         # 如果指定在一个空节点之前或者空链表之前插入数据节点，则什么都不做
            return

        if node == self.__head:                             # 如果是在链表头之前插入数据节点，则直接插入
            self.insert_to_head(value)
            return

        new_node = Node(value)
        pro = self.__head
        not_found = False                                   # 如果在整个链表中都没有找到指定插入的Node节点，则该标记为True
        while pro.next_node != node:                        # 寻找指定Node之前的一个Node
            if pro.next_node is None:                       # 如果已经到了链表的最后一个节点，则表明该链表中没有找到指定插入的Node节点
                not_found = True
                break
            else:
                pro = pro.next_node

        if not not_found:
            pro.next_node = new_node
            new_node.next_node = node


    def insert_last(self,value):
        """
        插入最后一个节点，然后指向的是头节点
        :return:
        """
        # 1. 先查找最后一个节点
        # 2. 插入最后一个节点并将节点指向头节点
        last_node = Node(value)
        self.__head=last_node.next_node

    def find_last_node(self):
        """
        查找最后一个节点
        :return:
        """
        if self.is_empty():
            return

        else:
            node = self.__head
            while node.next_node != self.__head:
                node = node.next_node

        return node


    def length_by_node(self):
        """
        链表长度
        :return:
        """
        pos = self.__head
        if pos is None:
            print("当前链表还没有数据")
            return

        count = 1
        while pos.next_node is not None and pos.next_node != self.__head:

            count+= 1
            pos = pos.next_node

        return count


    def delete_by_node(self, node):
        """在链表中删除指定Node的节点.
        参数:
            node:指定的Node节点
        """
        if self.__head is None:  # 如果链表是空的，则什么都不做
            return


        if node == self.__head:  # 如果指定删除的Node节点是链表的头节点，最后一个节点就要指向现在的头节点

            last_node = self.find_last_node()


            self.__head = node.next_node
            last_node.next_node = self.__head
            return

        pro = self.__head
        not_found = False  # 如果在整个链表中都没有找到指定删除的Node节点，则该标记量设置为True
        while pro.next_node != node:
            if pro.next_node == self.__head:  # 如果已经到链表的最后一个节点，则表明该链表中没有找到指定删除的Node节点
                not_found = True
                break
            else:
                pro = pro.next_node
        if not not_found:
            pro.next_node = node.next_node



    def create_node(self, value):
        """
        创建一个存储value值的Node节点
        参数：
            value:将要存储在Node节点中的数据
        返回：
            一个新的Node节点
        :param value:
        :return:
        """
        return Node(value)



    def print_all(self):
        """
        遍历整个链表
        :return:
        """
        pos = self.__head
        if pos is None:
            print("当前链表还没有数据")
            return

        list = []
        # 这里
        while pos.next_node is not None and pos.next_node != self.__head:
            list.append(pos.data)
            print(str(pos.data) + "--->", end="")
            pos = pos.next_node

        print(str(pos.data))
        list.append(pos.data)
        return list







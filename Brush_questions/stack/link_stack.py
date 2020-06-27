
# 使用链表实现栈
# 栈要实现的效果就是先进后出
class Node:
    """
    链表节点
    """
    def __init__(self, data=None, next=None):
        self.__data = data
        self.__next = next


class LinkedStack:
    def __init__(self):
        self.__top = None



    def push(self,value):
        new_node = Node(value)
        new_node.next = self.__top
        self.__top = new_node



    def pop(self):
        if self.__top:
            value = self.__top.__data
            self.__top = self.__top.next

class Stack():
    def __init__(self):
        # 初始化一个列表
        self.items = []

    def is_empty(self):
        # 是否为空
        if self.items == None:
            return True
        else:
            return False

    def push(self, value):
        # 把值放入栈
        self.items.append(value)

    def pop(self):
        """
        把最上面一个值取出
        :return:
        """
        if self.is_empty():
            return False

        else:
            self.items.pop()

    def top(self):
        """
        返回栈顶元素
        :return:
        """
        return self.items[len(self.items) - 1]


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.pop()
print(stack.items)




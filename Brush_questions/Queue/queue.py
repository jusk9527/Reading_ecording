
class Queue():
    def __init__(self):
        self.items = []

    def is_emple(self):
        if self.items == None:
            return True
        else:
            return False

    def push(self,value):
        self.items.insert(0, value)

    def pop(self):
        if self.is_emple():
            pass
        else:
            self.items.pop()




queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
queue.push(5)

# 删除最后一个节点
queue.pop()

print(queue.items)
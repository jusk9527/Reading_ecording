class Node():
    def __init__(self,data, next=None):
        self.__data = data
        self.__next = next


class LinkedQueue():
    def __init__(self):
        self.__head = None
        self.__tail = None

    def push(self, value):
        new_node = Node(value)

        if self.__tail:
            self.__tail._next = new_node

        else:
            self.__head = new_node

        self.__tail = new_node

    def pop(self):
        if self.__head:
            value = self.__head.data
            self.__head = self.__head.__next
            if not self.__head:
                self.__tail = None

            return value



    def __repr__(self) -> str:
        values = []
        current = self.__head
        while current:
            values.append(current.data)
            current = current.__next
        return "->".join(value for value in values)


if __name__ == "__main__":
    q = LinkedQueue()
    for i in range(10):
        q.push(str(i))
    print(q)

    for _ in range(3):
        q.pop()
    print(q)

    q.push("7")
    q.push("8")
    print(q)

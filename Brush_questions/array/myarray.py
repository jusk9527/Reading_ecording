class  MyArray():
    """
    自定义固定容器数组
    """
    def __init__(self,capacity:int):
        self._data = []
        self.capacity = capacity


    def __getitem__(self, position: int) -> object:
        return self._data[position]

    def __setitem__(self, index: int, value: object):
        self._data[index] = value

    def __len__(self):
        return len(self._data)


    def insert(self,index,value):
        if len(self)>=self.capacity:
            return False
        else:
            self._data.insert(index, value)

    def find(self, index):
        try:
            return self._data[index]
        except:
            return None

    def delete(self,index):
        try:
            return self._data.pop(index)
        except:
            return None

    def __iter__(self):
        for item in self._data:
            yield item


    def print_all(self):
        for item in self:
            print(item)

array = MyArray(10)
# array[1] = 3
# print(array[0])
array.insert(0,1)
array.insert(0,2)
# array[1] = 5
print(array._data)
print(array.find(0))
# array.print_all()
# print(array._data)


from collections import deque



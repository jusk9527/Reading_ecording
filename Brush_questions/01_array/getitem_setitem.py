
class DictDemo:
      def __init__(self,key,value):
            self.dict = {}
            self.dict[key] = value
      def __getitem__(self,key):
            return self.dict[key]
      def __setitem__(self,key,value):
            self.dict[key] = value
dictDemo = DictDemo('key0','value0')
print(dictDemo['key0']) #value0
dictDemo['key1'] = 'value1'
print(dictDemo["key1"])
# print(dictDemo['key2'])           # 报错


class ArrayDemo:
    def __init__(self, index, value):
        self.array = []
        self.array[index] = value

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, value):
        self.array[index] = value


dictDemo = DictDemo(0, 0)
print(dictDemo[0])  # value0
dictDemo[1] = 1
dictDemo[2] = 2
dictDemo[3] = 3

print(dictDemo[1])
print(dictDemo[2])
print(dictDemo[3])

# print(dictDemo['key2'])           # 报错


# value0
# value1
# 0
# 1
# 2
# 3

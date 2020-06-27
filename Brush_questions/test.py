from collections import OrderedDict


d = OrderedDict.fromkeys('abcde')


# 返回最后一个有序字典的键值对（LIFO  后进先出）
order_pop = d.popitem()
print(order_pop)

# 将现有key移动到字典任意一段
d.move_to_end('b')

order_key = ''.join(d.keys())
print(order_key)



d.move_to_end('b', last=False)

print(''.join(d.keys()))



print(d.items())

print(d.values())
print(d.keys())


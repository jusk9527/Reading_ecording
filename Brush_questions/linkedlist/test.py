import copy
list = [1,2,3]
print(id(list))

m = copy.copy(list)


print(id(m))
list.append(4)

print(id(list))

print(m)
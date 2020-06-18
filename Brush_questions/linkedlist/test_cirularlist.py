from Brush_questions.linkedlist.circular_list import CircularList


circularlist = CircularList()

node1 = circularlist.create_node(1)
node2 = circularlist.create_node(2)
node3 = circularlist.create_node(3)
node4 = circularlist.create_node(4)
node5 = circularlist.create_node(5)


node1.next_node = node2
node2.next_node = node3
node3.next_node = node4
node4.next_node = node5



circularlist.head = node1
node5.next_node = circularlist.head
print_a = circularlist.print_all()

print(print_a)



# 节点长度
count = circularlist.length_by_node()

print(count)



# 插入某个节点

circularlist.insert_after(node2,7)
circularlist.insert_after(node3,8)

print_a = circularlist.print_all()

print(print_a)


# 查找到最后一个节点
last_node = circularlist.find_last_node()
print(last_node)

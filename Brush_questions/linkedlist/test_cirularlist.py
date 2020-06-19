from Brush_questions.linkedlist.circular_list import CircularList


def the_some():
    """
    创建一个循环单链表
    :return:
    """
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

    return circularlist

def test_create_singlink():
    """
    创建链表
    :return:
    """
    circularlist = the_some()
    list = circularlist.print_all()
    assert list == [1,2,3,4,5]



def test_length_by_node():
    circularlist = the_some()
    length = circularlist.length_by_node()
    assert length == 5


def test_insert_after():
    """
    在某个节点之后插入某值
    :return:
    """
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

    circularlist.insert_after(node2,7)
    circularlist.insert_after(node3, 8)
    print_a = circularlist.print_all()
    assert print_a == [1,2,7,3,8,4,5]

def test_find_last_node():
    """
    查找最后一个节点
    :return:
    """
    circularlist = the_some()
    last_node = circularlist.find_last_node()
    assert last_node.data == 5

def test_find_by_value():
    """
    查找某值的节点
    :return:
    """
    circularlist = the_some()
    find_by_value = circularlist.find_by_value(5)
    assert find_by_value.data == 5

def test_find_by_index():
    """
    根据索引值查找某个节点
    :return:
    """
    circularlist = the_some()
    find_by_index = circularlist.find_by_value(4)
    assert find_by_index.data == 4

def test_insert_to_head():
    """
    插入到头节点
    :return:
    """
    circularlist = the_some()
    circularlist.insert_to_head(10)
    print_all = circularlist.print_all()
    assert print_all == [10,1,2,3,4,5]

def test_insert_after():
    """
    在某个节点插入某值
    :return:
    """
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
    # 在某个节点之后插入某值
    circularlist.insert_after(node2, 9)
    circularlist.insert_after(node5, 11)
    print_a = circularlist.print_all()
    assert print_a == [1,2,9,3,4,5,11]


def test_delete_by_node():
    """
    删除链表中的某个节点
    :return:
    """
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

    circularlist.delete_by_node(node1)
    print_a = circularlist.print_all()
    assert print_a == [2,3,4,5]


def test_insert_before():
    """
    在某个节点之前插入某值
    :return:
    """
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

    circularlist.insert_before(node3,9)

    print_a = circularlist.print_all()
    assert print_a == [1,2,9,3,4,5]




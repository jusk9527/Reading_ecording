from Brush_questions.linkedlist.singlyLinkedList import SinglyLinkedList



# 相似创建链表结构
def the_some():
    singlylink = SinglyLinkedList()
    head1 = singlylink.insert_to_head(1)
    node2 = singlylink.insert_after(head1, 2)
    node3 = singlylink.insert_after(node2, 3)
    node4 = singlylink.insert_after(node3, 4)
    node5 = singlylink.insert_after(node4, 5)


    return singlylink


def test_create_singlink():
    """
    创建链表
    :return:
    """
    singlylink = the_some()
    list = singlylink.print_all()
    assert list == [1,2,3,4,5]


def test_find_by_value():
    """
    寻找某值
    :return:
    """
    singlylink = the_some()
    list = singlylink.print_all()
    node = singlylink.find_by_value(2)

    assert list == [1, 2, 3, 4, 5]
    assert node.data == 2




def test_find_by_index():
    """
    寻找某索引的值
    :return:
    """
    singlylink = the_some()
    list = singlylink.print_all()
    node = singlylink.find_by_index(2)
    print("node节点是:"+str(node)+"\nand值是："+str(node.data))

    assert list == [1, 2, 3, 4, 5]
    assert node.data == 3


def test_insert_before():
    """
    插入某节点之前
    :return:
    """
    singlylink = SinglyLinkedList()
    head1 = singlylink.insert_to_head(1)
    node2 = singlylink.insert_after(head1, 2)
    node3 = singlylink.insert_after(node2, 3)
    node4 = singlylink.insert_after(node3, 4)
    node5 = singlylink.insert_after(node4, 5)
    list = singlylink.print_all()

    node6 = singlylink.insert_after(node5, 6)
    after = singlylink.print_all()

    node7 = singlylink.insert_before(node6,7)
    before = singlylink.print_all()

    assert list == [1,2,3,4,5]
    assert after == [1,2,3,4,5,6]
    assert before == [1,2,3,4,5,7,6]



def test_delete_by_node():
    """
    删除某节点
    :return:
    """
    singlylink = SinglyLinkedList()
    head = singlylink.insert_to_head(1)
    node = singlylink.insert_after(head, 2)
    node = singlylink.insert_after(node, 3)
    node = singlylink.insert_after(node, 4)
    node = singlylink.insert_after(node, 5)
    list = singlylink.print_all()

    node = singlylink.delete_by_node(node)
    delete_list = singlylink.print_all()

    assert list == [1,2,3,4,5]
    assert delete_list == [1,2,3,4]


def test_delete_last_n_node():
    """
    删除倒数第几个节点
    :return:
    """
    singlylink = the_some()
    list = singlylink.print_all()

    node = singlylink.delete_last_n_node(2)
    last_n_node = singlylink.print_all()

    assert list == [1,2,3,4,5]
    assert last_n_node == [1,2,3,5]


def test_reversed_self():
    """
    翻转链表
    :return:
    """
    singlylink = the_some()
    list = singlylink.print_all()

    node = singlylink.reversed_self()
    reversed_self = singlylink.print_all()

    assert list == [1,2,3,4,5]
    assert reversed_self == [5,4,3,2,1]


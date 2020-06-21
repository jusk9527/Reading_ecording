from Brush_questions.linkedlist.doublelink import DoubleLinkedList

def create_doublelinkedlist():
    double_link_list = DoubleLinkedList()
    double_link_list.append_last_by_node(1)
    double_link_list.append_last_by_node(2)
    double_link_list.append_last_by_node(3)
    double_link_list.append_last_by_node(4)
    double_link_list.append_last_by_node(5)



    return double_link_list


def test_create_doublelinkedlist():

    doublelinklist = create_doublelinkedlist()
    print_all = doublelinklist.print_all()
    assert print_all == [1,2,3,4,5]

def test_search_by_node():
    doublelinklist = create_doublelinkedlist()
    is_true_first = doublelinklist.search_by_node(2)
    is_true_second = doublelinklist.search_by_node(3)
    is_true_third = doublelinklist.search_by_node(9)


    assert is_true_first == True
    assert is_true_second == True
    assert is_true_third == False

def test_insert_before():
    """
    删除链表中第一个值为elem的节点
    :return:
    """
    doublelinklist = create_doublelinkedlist()
    doublelinklist.insert_before(1,6)
    print_all = doublelinklist.print_all()
    assert print_all == [1,6,2,3,4,5]

def test_remove_by_node():
    doublelinklist = create_doublelinkedlist()

    doublelinklist.remove_by_node(3)
    print_all = doublelinklist.print_all()
    assert print_all == [1, 2, 4, 5]

    doublelinklist.remove_by_node(9)
    print_all = doublelinklist.print_all()
    assert print_all == [1,2,4,5]


def test_insert_before():
    double_link_list = DoubleLinkedList()
    node1 = double_link_list.append_last_by_node(1)
    node2 = double_link_list.append_last_by_node(2)

    node3 = double_link_list.append_last_by_node(3)

    node4 = double_link_list.append_last_by_node(4)
    node5 = double_link_list.append_last_by_node(5)

    double_link_list.insert_before(node2,9)

    print_all = double_link_list.print_all()

    assert print_all == [1,9,2,3,4,5]




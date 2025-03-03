from src.sem2_stack_queue_etc.Linked_list import Node, LinkedList
from is_cycle import is_cycle

def test_empty_list():
    ll = LinkedList()
    assert is_cycle(ll) == False

def test_single_element_non_cyclic():
    ll = LinkedList()
    ll.append_back(1)
    assert is_cycle(ll) == False

def test_single_element_cyclic():
    ll = LinkedList()
    node = Node(1)
    ll.head = node
    node.next = node  # Замыкаем список на себя
    assert is_cycle(ll) == True

def test_multiple_elements_non_cyclic():
    ll = LinkedList()
    ll.append_back(1)
    ll.append_back(2)
    ll.append_back(3)
    assert is_cycle(ll) == False

def test_multiple_elements_cyclic_first():
    ll = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    ll.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node1  # Замыкаем список на первый элемент
    assert is_cycle(ll) == True

def test_multiple_elements_cyclic_middle():
    ll = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    ll.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Замыкаем список на второй элемент
    assert is_cycle(ll) == True

def test_multiple_elements_cyclic_last():
    ll = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    ll.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node4  # Замыкаем список на последний элемент
    assert is_cycle(ll) == True
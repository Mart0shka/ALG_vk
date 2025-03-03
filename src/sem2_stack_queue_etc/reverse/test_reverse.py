from src.sem2_stack_queue_etc.Linked_list import Node, LinkedList
from reverse import reverse

def test_reverse_empty_list():
    # Проверка на пустой список
    ll = LinkedList()
    ll = reverse(ll)
    assert ll.head is None

def test_reverse_single_element():
    # Проверка на список с одним элементом
    ll = LinkedList()
    ll.append_back(1)
    ll = reverse(ll)
    assert ll.head.data == 1
    assert ll.head.next is None


def test_reverse_multiple_elements():
    # Проверка на список с несколькими элементами
    ll = LinkedList()
    ll.append_back(1)
    ll.append_back(2)
    ll.append_back(3)
    ll.append_back(4)
    ll = reverse(ll)
    assert ll.head.data == 4
    assert ll.head.next.data == 3
    assert ll.head.next.next.data == 2
    assert ll.head.next.next.next.data == 1
    assert ll.head.next.next.next.next is None

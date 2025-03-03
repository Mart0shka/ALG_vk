from src.sem2_stack_queue_etc.Linked_list import Node, LinkedList
from find_mid import find_middle

def test_find_middle_empty_list():
    # Проверка на пустой список
    ll = LinkedList()
    assert find_middle(ll) == None

def test_find_middle_single_element():
    # Проверка на список с одним элементом
    ll = LinkedList()
    ll.append_back(1)  # Список: 1
    middle = find_middle(ll)
    assert middle.data == 1

def test_find_middle_two_elements():
    # Проверка на список с двумя элементами
    ll = LinkedList()
    ll.append_back(1)  # Список: 1 -> 2
    ll.append_back(2)
    middle = find_middle(ll)
    assert middle.data == 2

def test_find_middle_odd_elements():
    # Проверка на список с нечётным количеством элементов
    ll = LinkedList()
    ll.append_back(1)  # Список: 1 -> 2 -> 3
    ll.append_back(2)
    ll.append_back(3)
    middle = find_middle(ll)
    assert middle.data == 2

def test_find_middle_even_elements():
    # Проверка на список с чётным количеством элементов
    ll = LinkedList()
    ll.append_back(1)
    ll.append_back(2)
    ll.append_back(3)
    ll.append_back(4)
    middle = find_middle(ll)
    assert middle.data == 3

def test_find_middle_large_list():
    # Проверка на большой список
    ll = LinkedList()
    for i in range(1, 11):
        ll.append_back(i)
    middle = find_middle(ll)
    assert middle.data == 6
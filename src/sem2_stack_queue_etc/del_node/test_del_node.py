from src.sem2_stack_queue_etc.Linked_list import Node, LinkedList
from del_node import del_node

def test_del_node_empty_list():
    # Проверка на пустой список
    ll = LinkedList()
    new_ll = del_node(ll, 1)
    assert new_ll.to_list() == []

def test_del_node_no_match():
    # Проверка, если в списке нет элементов, равных val
    ll = LinkedList()
    ll.append_back(1)
    ll.append_back(2)
    ll.append_back(3)
    new_ll = del_node(ll, 4)
    assert new_ll.to_list() == [1, 2, 3]

def test_del_node_all_match():
    # Проверка, если все элементы списка равны val
    ll = LinkedList()
    ll.append_back(2)
    ll.append_back(2)
    ll.append_back(2)
    new_ll = del_node(ll, 2)
    assert new_ll.to_list() == []

def test_del_node_some_match():
    # Проверка, если некоторые элементы списка равны val
    ll = LinkedList()
    ll.append_back(1)
    ll.append_back(2)
    ll.append_back(3)
    ll.append_back(2)
    ll.append_back(4)
    new_ll = del_node(ll, 2)
    assert new_ll.to_list() == [1, 3, 4]

def test_del_node_head_match():
    # Проверка, если голова списка равна val
    ll = LinkedList()
    ll.append_back(1)
    ll.append_back(2)
    ll.append_back(3)
    new_ll = del_node(ll, 1)
    assert new_ll.to_list() == [2, 3]

def test_del_node_tail_match():
    # Проверка, если хвост списка равен val
    ll = LinkedList()
    ll.append_back(1)
    ll.append_back(2)
    ll.append_back(3)
    new_ll = del_node(ll, 3)
    assert new_ll.to_list() == [1, 2]

def test_del_node_multiple_matches():
    # Проверка, если в списке несколько элементов, равных val
    ll = LinkedList()
    ll.append_back(1)
    ll.append_back(2)
    ll.append_back(2)
    ll.append_back(3)
    ll.append_back(2)
    new_ll = del_node(ll, 2)
    assert new_ll.to_list() == [1, 3]
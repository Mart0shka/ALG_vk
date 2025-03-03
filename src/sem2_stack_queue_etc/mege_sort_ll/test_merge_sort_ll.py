from src.sem2_stack_queue_etc.Linked_list import Node, LinkedList
from merge_sort_ll import merge_sort_ll

def test_merge_sort_ll_both_empty():
    # Проверка на два пустых списка
    ll1 = LinkedList()
    ll2 = LinkedList()
    merged_ll = merge_sort_ll(ll1, ll2)
    assert merged_ll.to_list() == []

def test_merge_sort_ll_first_empty():
    # Проверка, если первый список пустой
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll2.append_back(1)
    ll2.append_back(2)
    merged_ll = merge_sort_ll(ll1, ll2)
    assert merged_ll.to_list() == [1, 2]

def test_merge_sort_ll_second_empty():
    # Проверка, если второй список пустой
    ll1 = LinkedList()
    ll1.append_back(1)
    ll1.append_back(2)
    ll2 = LinkedList()
    merged_ll = merge_sort_ll(ll1, ll2)
    assert merged_ll.to_list() == [1, 2]

def test_merge_sort_ll_simple():
    # Проверка на два простых списка
    ll1 = LinkedList()
    ll1.append_back(1)
    ll1.append_back(3)
    ll2 = LinkedList()
    ll2.append_back(2)
    ll2.append_back(4)
    merged_ll = merge_sort_ll(ll1, ll2)
    assert merged_ll.to_list() == [1, 2, 3, 4]

def test_merge_sort_ll_duplicates():
    # Проверка на списки с дублирующими элементами
    ll1 = LinkedList()
    ll1.append_back(1)
    ll1.append_back(3)
    ll1.append_back(3)
    ll2 = LinkedList()
    ll2.append_back(2)
    ll2.append_back(3)
    ll2.append_back(4)
    merged_ll = merge_sort_ll(ll1, ll2)
    assert merged_ll.to_list() == [1, 2, 3, 3, 3, 4]

def test_merge_sort_ll_large_lists():
    # Проверка на большие списки
    ll1 = LinkedList()
    for i in range(0, 100, 2):
        ll1.append_back(i)  # Чётные числа: 0, 2, 4, ..., 98
    ll2 = LinkedList()
    for i in range(1, 100, 2):
        ll2.append_back(i)  # Нечётные числа: 1, 3, 5, ..., 99
    merged_ll = merge_sort_ll(ll1, ll2)
    expected = list(range(100))
    assert merged_ll.to_list() == expected

def test_merge_sort_ll_one_element_each():
    # Проверка на списки с одним элементом
    ll1 = LinkedList()
    ll1.append_back(1)
    ll2 = LinkedList()
    ll2.append_back(2)
    merged_ll = merge_sort_ll(ll1, ll2)
    assert merged_ll.to_list() == [1, 2]
from src.sem2_stack_queue_etc.Linked_list import Node, LinkedList

"""
Написать функцию, которая принимает на вход два отсортированных односвязных списка и 
объединяет их в один отсортированный список. При этом затраты по памяти должны быть O(1)
"""

def merge_sort_ll(ll1: LinkedList, ll2: LinkedList):
    dummy = Node(None)
    dummy.next = ll1.head
    curr1 = ll1.head
    prev1 = dummy
    curr2 = ll2.head
    while curr1 is not None and curr2 is not None:
        if curr2.data < curr1.data:
            next2 = curr2.next
            prev1.next = curr2
            curr2.next = curr1
            prev1 = curr2
            curr2 = next2
        else:
            prev1 = curr1
            curr1 = curr1.next

    if curr1 is None:
        prev1.next = curr2

    ll1.head = dummy.next
    return ll1




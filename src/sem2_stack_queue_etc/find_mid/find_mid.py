from src.sem2_stack_queue_etc.Linked_list import Node, LinkedList

"""
Дан связный список. Необходимо найти середину списка. Сделать это необходимо за O(n) без дополнительных аллокаций
"""

def find_middle(ll: LinkedList):
    slow, fast = ll.head, ll.head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow
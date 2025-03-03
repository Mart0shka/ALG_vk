from src.sem2_stack_queue_etc.Linked_list import Node, LinkedList

"""
Необходимо написать функцию, которая принимает на вход односвязный список и разворачивает его.
"""

def reverse(ll: LinkedList):
    prev = None
    curr = ll.head
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    ll.head = prev
    return ll

from src.sem2_stack_queue_etc.Linked_list import Node, LinkedList

"""
Необходимо написать функцию, которая принимает на вход односвязный список
и некоторое целое число val. 
Необходимо удалить узел из списка, значение которого равно val.
"""
def del_node(ll: LinkedList, item):
    dummy = Node(None)
    dummy.next = ll.head
    prev = dummy
    curr = ll.head
    while curr is not None:
        if curr.data == item:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    ll.head = dummy.next
    return ll

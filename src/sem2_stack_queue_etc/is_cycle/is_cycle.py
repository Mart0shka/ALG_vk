from src.sem2_stack_queue_etc.Linked_list import Node, LinkedList
"""
Дан односвязный список. Необходимо проверить, является ли этот список циклическим.

Циклическим (кольцевым) списком называется список у которого последний узел ссылается на один из предыдущих узлов.

"""


def is_cycle(ll):
    if ll.head is None or ll.head.next is None:
        return False

    slow = ll.head
    fast = ll.head.next

    while slow!=fast:
        if fast is None or fast.next is None:
            return False
        fast = fast.next.next
        slow = slow.next

    return True



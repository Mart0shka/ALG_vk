class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        i = 0
        curr = self.head
        while curr is not None:
            i += 1
            curr = curr.next
        return i

    def __str__(self):
        res = ""
        curr = self.head
        while curr is not None:
            res+=f"{curr.data} -->  "
            curr = curr.next
        return res

    def append_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node
        return

    def append_back(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next

        curr_node.next = new_node
        return

    def to_list(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result





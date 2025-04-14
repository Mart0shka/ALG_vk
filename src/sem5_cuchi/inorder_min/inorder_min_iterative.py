def inorder_min_iterative(node, k):
    stack = []
    counter = 0
    current = node

    while len(stack)>0 or current is not None:
        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()
        counter+=1

        if counter == k:
            return current.data

        current = current.right

    return None
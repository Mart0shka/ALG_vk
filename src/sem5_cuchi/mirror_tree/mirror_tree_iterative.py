from collections import deque

def mirror_tree_iterative(node):
    if node is None:
        return None

    queue = deque([node])

    while len(queue)>0:
        current = queue.pop()

        current.left, current.right = current.right, current.left

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return node
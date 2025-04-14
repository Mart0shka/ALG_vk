from collections import deque
def is_max_heap_BFS(root):
    if root is None:
        return True

    queue = deque([root])
    should_be_leaf = False

    while len(queue) > 0:
        curr = queue.popleft()

        if curr.left:
            if should_be_leaf or curr.left.data > curr.data:
                return False

            queue.append(curr.left)
        else:
            should_be_leaf = True

        if curr.right:
            if should_be_leaf or curr.right.data > curr.data:
                return False

            queue.append(curr.right)
        else:
            should_be_leaf = True

    return True

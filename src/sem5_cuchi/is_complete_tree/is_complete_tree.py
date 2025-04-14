from collections import deque

def is_complete_tree(root):
    if root is None:
        return True

    queue = deque([root])
    should_be_leaf = False

    while len(queue)>0:
        node = queue.popleft()

        if node is None:
            should_be_leaf = True
        else:
            if should_be_leaf:
                return False

            queue.append(node.left)
            queue.append(node.right)

    return True
from sympy import false


def is_symmetricBFS(root):
    if root is None:
        return True
    queue = [root]

    while len(queue)>0:
        queue_len = len(queue)
        for i in range(queue_len):
            if queue[i] is None and queue[queue_len-i-1] is None:
                continue
            if queue[i] is None or queue[queue_len-i-1] is None:
                return False
            if queue[i].data != queue[queue_len-i-1].data:
                return False
            queue.append(queue[i].left)
            queue.append(queue[i].right)

        queue = queue[queue_len:]

    return True
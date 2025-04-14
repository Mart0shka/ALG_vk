def inorder_min(node, k, counter=0):  # Используем изменяемый объект (список)
    if node is None:
        return None

    left_res = inorder_min(node.left, k, counter)
    if left_res is not None:
        return left_res

    counter += 1  # Изменяем значение по ссылке

    if counter == k:
        return node.data

    return inorder_min(node.right, k, counter)
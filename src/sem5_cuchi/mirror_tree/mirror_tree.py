def mirror_tree(node):
    if node is None:
        return None

    node.left, node.right = node.right, node.left

    mirror_tree(node.left)
    mirror_tree(node.right)

    return node
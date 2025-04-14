def min_height(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.left is not None and root.right is not None:
        return 1 + min(min_height(root.left), min_height(root.right))
    if root.left is not None:
        return 1 + min_height(root.left)
    if root.right is not None:
        return 1 + min_height(root.right)

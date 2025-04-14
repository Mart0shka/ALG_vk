def dfs(left, right):
    if left is None or right is None:
        return 0

    count = 0

    if left.data == right.data:
        count = 1

    count += dfs(left.left, right.right)
    count += dfs(left.right, right.left)

    return count

def count_mirror_twins(root):
    if root is None:
        return 0
    return dfs(root.left, root.right)
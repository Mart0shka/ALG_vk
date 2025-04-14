from src.sem4_binary_tree.binary_tree import TreeNode


def build_tree(arr,i):
    if i>=len(arr):
        return None

    root = TreeNode(arr[i])
    root.left = build_tree(arr, 2 * i + 1)
    root.right = build_tree(arr, 2 * i + 2)

    return root


from src.sem4_binary_tree.binary_tree import TreeNode
from src.sem4_binary_tree.mirror_node.mirror_node_sem import count_mirror_twins

def test_single_pair():
    # Структура дерева:
    #     1
    #   /   \
    #  2     2
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    assert count_mirror_twins(root) == 1

def test_no_mirror_pairs():
    # Структура дерева:
    #     1
    #   /   \
    #  2     3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert count_mirror_twins(root) == 0

def test_multiple_pairs():
    # Структура дерева:
    #        3
    #      /   \
    #     9     9
    #    / \   / \
    #   6   8 8   6
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(9)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(8)
    root.right.right = TreeNode(6)
    assert count_mirror_twins(root) == 3  # Пары: (9,9), (6,6), (8,8)

def test_empty_tree():
    root = None
    assert count_mirror_twins(root) == 0

def test_partial_mirror():
    # Структура дерева:
    #        5
    #      /   \
    #     3     3
    #    /       \
    #   4         4
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(4)
    assert count_mirror_twins(root) == 2  # Пары: (3,3), (4,4)
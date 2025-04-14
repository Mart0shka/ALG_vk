from src.sem4_binary_tree.find_min_height.find_min_height import min_height
from src.sem4_binary_tree.binary_tree import TreeNode

def test_empty_tree():
    assert min_height(None) == 0

def test_single_node():
    root = TreeNode(1)
    assert min_height(root) == 1


def test_balanced_tree():
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    assert min_height(root) == 2


def test_unbalanced_tree():
    #        1
    #       /
    #      2
    #     / \
    #    4   5
    #   /
    #  6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)

    assert min_height(root) == 3


def test_mixed_depth_tree():
    #        1
    #       / \
    #      2   3
    #           \
    #            4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)

    assert min_height(root) == 2


def test_early_leaf():
    #        1
    #       / \
    #      2   3
    #     /     \
    #    4       5
    #   /
    #  6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(6)

    assert min_height(root) == 3  # Самый короткий путь: 1 → 3 → 5
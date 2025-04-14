from src.sem5_cuchi.is_complete_tree.is_complete_tree import is_complete_tree
from src.sem4_binary_tree.binary_tree import TreeNode

def test_empty_tree():
    assert is_complete_tree(None) == True

def test_single_node():
    root = TreeNode(1)
    assert is_complete_tree(root) == True

def test_complete_tree():
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
    assert is_complete_tree(root) == True

def test_incomplete_last_level():
    #        1
    #       / \
    #      2   3
    #     /     \
    #    4       6  # Пропуск 5 слева
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(6)
    assert is_complete_tree(root) == False

def test_not_full_levels():
    #        1
    #       / \
    #      2   3
    #     /
    #    4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    assert is_complete_tree(root) == True

def test_complete_unbalanced():
    #        1
    #       /
    #      2
    #     / \
    #    3   4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    assert is_complete_tree(root) == False

def test_large_complete_tree():
    #          1
    #        /   \
    #       2     3
    #      / \   / \
    #     4  5 6   7
    #    / \
    #   8   9
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    assert is_complete_tree(root) == True

def test_missing_inner_node():
    #        1
    #       / \
    #      2   3
    #       \
    #        5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    assert is_complete_tree(root) == False

def test_complete_with_null_right():
    #        1
    #       /
    #      2
    root = TreeNode(1)
    root.left = TreeNode(2)
    assert is_complete_tree(root) == True
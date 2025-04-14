from src.sem5_cuchi.inorder_min.inorder_min_iterative import inorder_min_iterative
from src.sem4_binary_tree.binary_tree import TreeNode


def test_empty_tree():
    assert inorder_min_iterative(None, 1) is None


def test_single_node():
    root = TreeNode(5)
    assert inorder_min_iterative(root, 1) == 5
    assert inorder_min_iterative(root, 2) is None  # k превышает размер дерева


def test_small_tree():
    #     3
    #    / \
    #   1   4
    #    \
    #     2
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    assert inorder_min_iterative(root, 1) == 1  # 1-й наименьший
    assert inorder_min_iterative(root, 2) == 2  # 2-й наименьший
    assert inorder_min_iterative(root, 3) == 3  # 3-й наименьший
    assert inorder_min_iterative(root, 4) == 4  # 4-й наименьший
    assert inorder_min_iterative(root, 5) is None  # k превышает размер дерева


def test_unbalanced_tree():
    #     5
    #    /
    #   3
    #  /
    # 1
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)

    assert inorder_min_iterative(root, 1) == 1
    assert inorder_min_iterative(root, 2) == 3
    assert inorder_min_iterative(root, 3) == 5
    assert inorder_min_iterative(root, 4) is None


def test_large_tree():
    #          4
    #        /   \
    #       2     6
    #      / \   / \
    #     1   3 5   7
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)

    assert inorder_min_iterative(root, 1) == 1
    assert inorder_min_iterative(root, 3) == 3
    assert inorder_min_iterative(root, 5) == 5
    assert inorder_min_iterative(root, 7) == 7
    assert inorder_min_iterative(root, 8) is None


def test_k_zero_or_negative():
    root = TreeNode(1)
    assert inorder_min_iterative(root, 0) is None
    assert inorder_min_iterative(root, -1) is None
from src.sem5_cuchi.inorder_min.inorder_min import inorder_min
from src.sem4_binary_tree.binary_tree import TreeNode


def test_empty_tree():
    assert inorder_min(None, 1, 0) is None


def test_single_node():
    root = TreeNode(5)
    assert inorder_min(root, 1, 0) == 5
    assert inorder_min(root, 2, 0) is None  # k превышает размер дерева


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

    assert inorder_min(root, 1, 0) == 1  # 1-й наименьший
    assert inorder_min(root, 2, 0) == 2  # 2-й наименьший
    assert inorder_min(root, 3, 0) == 3  # 3-й наименьший
    assert inorder_min(root, 4, 0) == 4  # 4-й наименьший
    assert inorder_min(root, 5, 0) is None  # k превышает размер дерева


def test_unbalanced_tree():
    #     5
    #    /
    #   3
    #  /
    # 1
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)

    assert inorder_min(root, 1, 0) == 1
    assert inorder_min(root, 2, 0) == 3
    assert inorder_min(root, 3, 0) == 5
    assert inorder_min(root, 4, 0) is None


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

    assert inorder_min(root, 1, 0) == 1
    assert inorder_min(root, 3, 0) == 3
    assert inorder_min(root, 5, 0) == 5
    assert inorder_min(root, 7, 0) == 7
    assert inorder_min(root, 8, 0) is None


def test_k_zero_or_negative():
    root = TreeNode(1)
    assert inorder_min(root, 0, 0) is None
    assert inorder_min(root, -1, 0) is None
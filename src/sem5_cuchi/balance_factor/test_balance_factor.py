from src.sem4_binary_tree.binary_tree import TreeNode
from src.sem5_cuchi.balance_factor.balance_factor import calculate_heights_and_balances


def test_empty_tree():
    root = None
    calculate_heights_and_balances(root)
    assert root is None


def test_single_node():
    root = TreeNode(5)
    calculate_heights_and_balances(root)
    assert root.balance_factor == 0


def test_balanced_tree():
    #       5
    #      / \
    #     3   7
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    calculate_heights_and_balances(root)
    assert root.balance_factor == 0
    assert root.left.balance_factor == 0
    assert root.right.balance_factor == 0


def test_left_heavy_tree():
    #       5
    #      /
    #     3
    #    /
    #   1
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    calculate_heights_and_balances(root)
    assert root.balance_factor == 2
    assert root.left.balance_factor == 1
    assert root.left.left.balance_factor == 0


def test_right_heavy_tree():
    #       5
    #        \
    #         7
    #          \
    #           9
    root = TreeNode(5)
    root.right = TreeNode(7)
    root.right.right = TreeNode(9)
    calculate_heights_and_balances(root)
    assert root.balance_factor == -2
    assert root.right.balance_factor == -1
    assert root.right.right.balance_factor == 0


def test_complex_tree():
    #        10
    #       /  \
    #      5    15
    #     / \     \
    #    3   7     20
    #   /     \
    #  1       9
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(20)
    root.left.left.left = TreeNode(1)
    root.left.right.right = TreeNode(9)

    calculate_heights_and_balances(root)


    assert root.balance_factor == 1
    assert root.left.balance_factor == 0
    assert root.right.balance_factor == -1
    assert root.left.left.balance_factor == 1
    assert root.left.right.balance_factor == -1
    assert root.right.right.balance_factor == 0
    assert root.left.left.left.balance_factor == 0
    assert root.left.right.right.balance_factor == 0


def test_tree_with_negative_values():
    #       0
    #      / \
    #    -1   1
    #    /     \
    #  -2       2
    root = TreeNode(0)
    root.left = TreeNode(-1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(-2)
    root.right.right = TreeNode(2)

    calculate_heights_and_balances(root)

    assert root.balance_factor == 0
    assert root.left.balance_factor == 1
    assert root.right.balance_factor == -1
    assert root.left.left.balance_factor == 0
    assert root.right.right.balance_factor == 0
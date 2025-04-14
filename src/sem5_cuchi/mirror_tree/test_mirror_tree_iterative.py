from src.sem5_cuchi.mirror_tree.mirror_tree_iterative import mirror_tree_iterative
from src.sem4_binary_tree.binary_tree import TreeNode

def test_empty_tree():
    assert mirror_tree_iterative(None) is None


def test_single_node():
    root = TreeNode(1)
    mirrored = mirror_tree_iterative(root)
    assert mirrored.data == 1
    assert mirrored.left is None
    assert mirrored.right is None


def test_simple_tree():
    # Исходное:  1    Зеркало:  1
    #           /               \
    #          2                 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    mirrored = mirror_tree_iterative(root)

    assert mirrored.data == 1
    assert mirrored.left is None
    assert mirrored.right.data == 2


def test_complex_tree():

    # Исходное:      1          Зеркало:     1
    #             /     \                  /     \
    #           2        3               3        2
    #          / \      /               /        / \
    #         4   5    6               6        5   4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    mirrored = mirror_tree_iterative(root)


    assert mirrored.data == 1

    assert mirrored.left.data == 3
    assert mirrored.right.data == 2

    assert mirrored.left.right.data == 6
    assert mirrored.right.left.data == 5
    assert mirrored.right.right.data == 4


def test_unbalanced_tree():
    # Исходное:  1      Зеркало:  1
    #             \              /
    #              2           2
    #               \         /
    #                3       3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)

    mirrored = mirror_tree_iterative(root)

    assert mirrored.data == 1
    assert mirrored.right is None
    assert mirrored.left.data == 2
    assert mirrored.left.right is None
    assert mirrored.left.left.data == 3


def test_tree_with_single_child_nodes():
    # Исходное:    1      Зеркало:    1
    #             /                  /
    #           2                  2
    #            \                /
    #             3              3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)

    mirrored = mirror_tree_iterative(root)

    assert mirrored.data == 1
    assert mirrored.right.data == 2
    assert mirrored.right.left.data == 3


def test_mirror_twice():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    mirrored_once = mirror_tree_iterative(root)
    mirrored_twice = mirror_tree_iterative(mirrored_once)

    assert mirrored_twice.data == root.data
    assert mirrored_twice.left.data == root.left.data
    assert mirrored_twice.right.data == root.right.data
    assert mirrored_twice.left.left.data == root.left.left.data
    assert mirrored_twice.left.right.data == root.left.right.data

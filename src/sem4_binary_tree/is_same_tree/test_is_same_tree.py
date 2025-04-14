from src.sem4_binary_tree.is_same_tree.is_same_tree import is_same_tree
from src.sem4_binary_tree.binary_tree import TreeNode


def test_both_trees_empty():
    assert is_same_tree(None, None) == True


def test_one_tree_empty():
    root = TreeNode(1)
    assert is_same_tree(root, None) == False
    assert is_same_tree(None, root) == False


def test_single_node_same():
    a = TreeNode(5)
    b = TreeNode(5)
    assert is_same_tree(a, b) == True


def test_single_node_different():
    a = TreeNode(5)
    b = TreeNode(10)
    assert is_same_tree(a, b) == False


def test_same_structure_and_values():
    #        1               1
    #       / \             / \
    #      2   3           2   3
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)

    b = TreeNode(1)
    b.left = TreeNode(2)
    b.right = TreeNode(3)

    assert is_same_tree(a, b) == True


def test_same_structure_different_values():
    #        1               1
    #       / \             / \
    #      2   3           2   4
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)

    b = TreeNode(1)
    b.left = TreeNode(2)
    b.right = TreeNode(4)  # Значение изменено

    assert is_same_tree(a, b) == False


def test_different_structure():
    #        1               1
    #       /               / \
    #      2               2   3
    a = TreeNode(1)
    a.left = TreeNode(2)

    b = TreeNode(1)
    b.left = TreeNode(2)
    b.right = TreeNode(3)  # Добавлен правый узел

    assert is_same_tree(a, b) == False


def test_different_leaf_values():
    #        1               1
    #       / \             / \
    #      2   3           2   3
    #     /               /
    #    4               5
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)
    a.left.left = TreeNode(4)

    b = TreeNode(1)
    b.left = TreeNode(2)
    b.right = TreeNode(3)
    b.left.left = TreeNode(5)  # Значение листа изменено

    assert is_same_tree(a, b) == False


def test_mirror_trees():
    #        1               1
    #       / \             / \
    #      2   3           3   2
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)

    b = TreeNode(1)
    b.left = TreeNode(3)
    b.right = TreeNode(2)

    assert is_same_tree(a, b) == False  # Структура отличается!


def test_complex_trees():
    #          10                  10
    #        /   \               /   \
    #       5     15            5     15
    #      / \   / \           / \   / \
    #     1  7 12  20        1  7 12  20
    a = TreeNode(10)
    a.left = TreeNode(5)
    a.right = TreeNode(15)
    a.left.left = TreeNode(1)
    a.left.right = TreeNode(7)
    a.right.left = TreeNode(12)
    a.right.right = TreeNode(20)

    b = TreeNode(10)
    b.left = TreeNode(5)
    b.right = TreeNode(15)
    b.left.left = TreeNode(1)
    b.left.right = TreeNode(7)
    b.right.left = TreeNode(12)
    b.right.right = TreeNode(20)

    assert is_same_tree(a, b) == True
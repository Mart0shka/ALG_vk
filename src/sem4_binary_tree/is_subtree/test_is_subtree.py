from src.sem4_binary_tree.is_subtree.is_subtree import is_subtree
from src.sem4_binary_tree.binary_tree import TreeNode


def test_both_empty():
    assert is_subtree(None, None) == True


def test_a_empty_b_not():
    b = TreeNode(1)
    assert is_subtree(None, b) == False


def test_b_empty():
    a = TreeNode(1)
    assert is_subtree(a, None) == True  # Зависит от спецификации!


def test_same_trees():
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)

    b = TreeNode(1)
    b.left = TreeNode(2)
    b.right = TreeNode(3)

    assert is_subtree(a, b) == True


def test_subtree_in_left():
    # Структура `a`:
    #        10
    #       /  \
    #      5    15
    #     / \
    #    3   7
    #   /
    #  2
    a = TreeNode(10)
    a.left = TreeNode(5)
    a.right = TreeNode(15)
    a.left.left = TreeNode(3)
    a.left.right = TreeNode(7)
    a.left.left.left = TreeNode(2)

    # Поддерево `b`:
    #      5
    #     / \
    #    3   7
    #   /
    #  2
    b = TreeNode(5)
    b.left = TreeNode(3)
    b.right = TreeNode(7)
    b.left.left = TreeNode(2)

    assert is_subtree(a, b) == True


def test_subtree_in_right():
    # Структура `a`:
    #        10
    #       /  \
    #      5    15
    #          / \
    #         12  20
    a = TreeNode(10)
    a.left = TreeNode(5)
    a.right = TreeNode(15)
    a.right.left = TreeNode(12)
    a.right.right = TreeNode(20)

    # Поддерево `b`:
    #      15
    #     / \
    #    12 20
    b = TreeNode(15)
    b.left = TreeNode(12)
    b.right = TreeNode(20)

    assert is_subtree(a, b) == True


def test_partial_match():
    # Структура `a`:
    #        10
    #       /  \
    #      5    15
    #     /
    #    3
    a = TreeNode(10)
    a.left = TreeNode(5)
    a.right = TreeNode(15)
    a.left.left = TreeNode(3)

    # Поддерево `b`:
    #      5
    #       \
    #        3
    b = TreeNode(5)
    b.right = TreeNode(3)  # В `a` узел 5 имеет левого потомка 3, а не правого

    assert is_subtree(a, b) == False


def test_multiple_matching_roots():
    # Структура `a`:
    #        10
    #       /  \
    #      5    5
    #     /     \
    #    3       3
    a = TreeNode(10)
    a.left = TreeNode(5)
    a.right = TreeNode(5)
    a.left.left = TreeNode(3)
    a.right.right = TreeNode(3)

    # Поддерево `b`:
    #      5
    #       \
    #        3
    b = TreeNode(5)
    b.right = TreeNode(3)

    assert is_subtree(a, b) == True  # Правое поддерево узла 5 в `a` совпадает с `b`



def test_b_deeper_than_a():
    # Структура `a`:
    #        5
    #       /
    #      3
    a = TreeNode(5)
    a.left = TreeNode(3)

    # Поддерево `b`:
    #      3
    #     /
    #    1
    b = TreeNode(3)
    b.left = TreeNode(1)

    assert is_subtree(a, b) == False


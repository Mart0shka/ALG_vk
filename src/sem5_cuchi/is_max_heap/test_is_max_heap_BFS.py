from src.sem5_cuchi.is_max_heap.is_max_heap_BFS import is_max_heap_BFS
from src.sem4_binary_tree.binary_tree import TreeNode

def test_empty_tree():
    assert is_max_heap_BFS(None) == True

def test_single_node():
    root = TreeNode(10)
    assert is_max_heap_BFS(root) == True

def test_valid_max_heap():
    #        9
    #       / \
    #      5   3
    #     / \
    #    1   4
    root = TreeNode(9)
    root.left = TreeNode(5)
    root.right = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    assert is_max_heap_BFS(root) == True

def test_invalid_max_heap():
    #        5
    #       / \
    #      9   3
    root = TreeNode(5)
    root.left = TreeNode(9)
    root.right = TreeNode(3)
    assert is_max_heap_BFS(root) == False

def test_valid_with_duplicates():
    #        8
    #       / \
    #      8   5
    root = TreeNode(8)
    root.left = TreeNode(8)
    root.right = TreeNode(5)
    assert is_max_heap_BFS(root) == True

def test_invalid_deep_nesting():
    #        10
    #       /  \
    #      5    9
    #     / \
    #    6   3  #
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(9)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(3)
    assert is_max_heap_BFS(root) == False


def test_invalid_right_child():
    #        10
    #       /  \
    #      5    15  # Нарушение: 15 > 10
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    assert is_max_heap_BFS(root) == False


def test_large_valid_heap():
    #          100
    #        /     \
    #      99      98
    #     /  \    /  \
    #    97  96 95  94
    root = TreeNode(100)
    root.left = TreeNode(99)
    root.right = TreeNode(98)
    root.left.left = TreeNode(97)
    root.left.right = TreeNode(96)
    root.right.left = TreeNode(95)
    root.right.right = TreeNode(94)
    assert is_max_heap_BFS(root) == True
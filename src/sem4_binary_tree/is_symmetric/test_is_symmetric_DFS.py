from src.sem4_binary_tree.binary_tree import TreeNode
from src.sem4_binary_tree.is_symmetric.is_symmetric_DFS import is_symmetricDFS
from src.sem4_binary_tree.is_symmetric.is_symmetric_BFS import is_symmetricBFS

def test_single_node():
    root = TreeNode(1)
    assert is_symmetricDFS(root) == True

def test_symmetric_tree():
    #        1
    #       / \
    #      2   2
    #     / \ / \
    #    3  4 4  3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    assert is_symmetricDFS(root) == True

def test_asymmetric_tree():
    #        1
    #       / \
    #      2   2
    #       \   \
    #        3   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)

    assert is_symmetricDFS(root) == False

def test_partially_symmetric_tree():
    #        1
    #       / \
    #      2   2
    #     /   /
    #    3   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(3)

    assert is_symmetricDFS(root) == False

def test_symmetric_structure_but_different_values():
    #        1
    #       / \
    #      2   2
    #     / \ / \
    #    3  4 5  3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)  # Не совпадает с left.right (4 != 5)
    root.right.right = TreeNode(3)

    assert is_symmetricDFS(root) == False
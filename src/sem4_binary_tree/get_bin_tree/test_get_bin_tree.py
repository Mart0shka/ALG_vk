from  src.sem4_binary_tree.binary_tree import TreeNode, get_array_from_tree
from  src.sem4_binary_tree.get_bin_tree.get_bin_tree import build_tree



def test_single_node():
    # Проверка на дерево с одним узлом
    root = TreeNode(1)
    assert get_array_from_tree(root) == [1]

    arr = [1]
    tree = build_tree(arr, 0)
    assert tree.data == 1
    assert tree.left is None
    assert tree.right is None


def test_complete_binary_tree():
    # Проверка на полное бинарное дерево
    arr = [1, 2, 3, 4, 5, 6, 7]
    tree = build_tree(arr, 0)

    # Проверяем структуру дерева
    assert tree.data == 1
    assert tree.left.data == 2
    assert tree.right.data == 3
    assert tree.left.left.data == 4
    assert tree.left.right.data == 5
    assert tree.right.left.data == 6
    assert tree.right.right.data == 7

    # Проверяем обратное преобразование
    assert get_array_from_tree(tree) == arr


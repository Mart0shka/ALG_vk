from is_tree import is_tree

def test_tree_simple():
    """Простой граф — дерево"""
    graph = {
        1: [2, 3],
        2: [1, 4],
        3: [1],
        4: [2]
    }
    assert is_tree(graph, 1) == True

def test_tree_with_cycle():
    """Граф с циклом — не дерево"""
    graph = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2]
    }
    assert is_tree(graph, 1) == False

def test_tree_disconnected():
    """Граф не связный — не дерево"""
    graph = {
        1: [2],
        2: [1],
        3: []
    }
    assert is_tree(graph, 1) == False

def test_tree_single_node():
    """Одна вершина без рёбер — корректное дерево"""
    graph = {
        1: []
    }
    assert is_tree(graph, 1) == True

def test_tree_two_components():
    """Две несвязные компоненты без циклов — не дерево"""
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3]
    }
    assert is_tree(graph, 1) == False

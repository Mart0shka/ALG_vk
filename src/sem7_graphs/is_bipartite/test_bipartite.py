from is_bipartite_bfs import is_bipartite_bfs
from is_bipartite_dfs import is_bipartite_dfs

def test_bipartite_simple():
    """Простой двудольный граф"""
    graph = {
        1: [2],
        2: [1, 3],
        3: [2]
    }
    assert is_bipartite_bfs(graph) == True
    assert is_bipartite_dfs(graph) == True

def test_bipartite_odd_cycle():
    """Нечётный цикл — граф не двудольный"""
    graph = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2]
    }
    assert is_bipartite_bfs(graph) == False
    assert is_bipartite_dfs(graph) == False

def test_bipartite_even_cycle():
    """Чётный цикл — граф двудольный"""
    graph = {
        1: [2, 4],
        2: [1, 3],
        3: [2, 4],
        4: [1, 3]
    }
    assert is_bipartite_bfs(graph) == True
    assert is_bipartite_dfs(graph) == True

def test_bipartite_disconnected_true():
    """Несвязный граф — каждая компонента двудольна"""
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3]
    }
    assert is_bipartite_bfs(graph) == True
    assert is_bipartite_dfs(graph) == True

def test_bipartite_disconnected_false():
    """Несвязный граф, одна компонента не двудольна"""
    graph = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2],
        4: [5],
        5: [4]
    }
    assert is_bipartite_bfs(graph) == False
    assert is_bipartite_dfs(graph) == False

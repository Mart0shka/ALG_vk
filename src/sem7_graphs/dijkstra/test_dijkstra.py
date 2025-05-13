from dijkstra import dijkstra

def test_dijkstra_basic():
    """Простой граф без циклов"""
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2, 'D': 3},
        'C': {'D': 1},
        'D': {}
    }
    assert dijkstra(graph, 'A') == {
        'A': 0, 'B': 1, 'C': 3, 'D': 4
    }

def test_dijkstra_start_alone():
    """Стартовая вершина не соединена ни с кем"""
    graph = {
        'A': {},
        'B': {'C': 1},
        'C': {}
    }
    expected = {'A': 0, 'B': float('inf'), 'C': float('inf')}
    assert dijkstra(graph, 'A') == expected

def test_dijkstra_unreachable_node():
    """В графе есть вершина, недостижимая из старта"""
    graph = {
        'A': {'B': 2},
        'B': {'C': 2},
        'C': {},
        'D': {'A': 1}  # 'D' изолирована от старта
    }
    expected = {'A': 0, 'B': 2, 'C': 4, 'D': float('inf')}
    assert dijkstra(graph, 'A') == expected

def test_dijkstra_with_cycle():
    """Граф с циклом"""
    graph = {
        'A': {'B': 1},
        'B': {'C': 1},
        'C': {'A': 1, 'D': 1},
        'D': {}
    }
    expected = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    assert dijkstra(graph, 'A') == expected

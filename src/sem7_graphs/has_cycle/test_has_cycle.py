from has_cycle import has_cycle

def test_empty_graph():
    """Пустой граф не содержит циклов"""
    assert has_cycle({}) == False

def test_single_node():
    """Граф с одной вершиной без рёбер"""
    assert has_cycle({1: []}) == False


def test_tree_structure():
    """Дерево (циклов нет)"""
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [],
        4: [],
        5: []
    }
    assert has_cycle(graph) == False

def test_has_cycle():
    """Граф содержит цикл"""
    graph = {
        1: [2],
        2: [3],
        3: [1]  # Цикл 1-2-3-1
    }
    assert has_cycle(graph) == True

def test_disconnected_graph_no_cycle():
    """Несвязный граф без циклов"""
    graph = {
        1: [2],
        2: [],
        3: [4],
        4: [],
        5: []
    }
    assert has_cycle(graph) == False

def test_multiple_cycles():
    """Граф с несколькими циклами"""
    graph = {
        1: [2, 3],
        2: [1, 3, 4],
        3: [1, 2, 4],
        4: [2, 3, 5, 6],
        5: [4, 6],
        6: [4, 5]
    }
    assert has_cycle(graph) == True

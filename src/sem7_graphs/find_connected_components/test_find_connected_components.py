from finc_connected_components_color import find_connected_components_color
from find_connected_components import find_connected_components
def test_empty_graph1():
    # Пустой граф
    assert find_connected_components_color({}) == {}

def test_single_node1():
    # Граф с одной вершиной
    graph = {1: []}
    result = find_connected_components_color(graph)
    assert result == {1: 1}

def test_two_isolated_nodes1():
    # Две изолированные вершины
    graph = {1: [], 2: []}
    result = find_connected_components_color(graph)
    assert result == {1: 1, 2: 2} or result == {1: 2, 2: 1}

def test_two_connected_nodes1():
    # Две соединенные вершины
    graph = {1: [2], 2: [1]}
    result = find_connected_components_color(graph)
    assert result == {1: 1, 2: 1}

def test_disconnected_graph1():
    # Несвязный граф с 3 компонентами
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3],
        5: [6, 7],
        6: [5],
        7: [5]
    }
    result = find_connected_components_color(graph)
    assert result[1] == result[2]
    assert result[3] == result[4]
    assert result[5] == result[6] == result[7]

def test_empty_graph():
    # Пустой граф
    assert find_connected_components({}) == []

def test_single_node():
    # Граф с одной вершиной
    graph = {1: []}
    result = find_connected_components(graph)
    assert result == [[1]] or result == [[1]]

def test_two_isolated_nodes():
    # Две изолированные вершины
    graph = {1: [], 2: []}
    result = find_connected_components(graph)
    assert len(result) == 2
    assert {1, 2} == {node for component in result for node in component}

def test_two_connected_nodes():
    # Две соединенные вершины
    graph = {1: [2], 2: [1]}
    result = find_connected_components(graph)
    assert result == [[1, 2]] or result == [[2, 1]]

def test_disconnected_graph():
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3],
        5: [6, 7],
        6: [5],
        7: [5]
    }
    result = find_connected_components(graph)
    assert len(result) == 3
    components = [set(comp) for comp in result]
    assert {1, 2} in components
    assert {3, 4} in components
    assert {5, 6, 7} in components


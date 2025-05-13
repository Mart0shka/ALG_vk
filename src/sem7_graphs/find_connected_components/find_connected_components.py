'''
Дан граф. Необходимо подсчитать
количество компонент связности.
'''

def find_connected_components(graph):
    visited = {node: False for node in graph}
    connected_components = []

    for node in graph:
        if not visited[node]:
            component = []
            dfs(graph, node, visited, component)
            connected_components.append(component)

    return connected_components


def dfs(graph, v, visited, component):
    visited[v] = True
    component.append(v)

    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, component)


def dfs(graph, v, visited, color):
    visited[v] = color
    for neighbor in graph[v]:
        if visited[neighbor] == 0:
            dfs(graph, neighbor, visited, color)


def find_connected_components_color(graph):
    visited = {node: 0 for node in graph}
    color = 0

    for node in graph:
        if visited[node] == 0:
            color += 1
            dfs(graph, node, visited, color)

    return visited
'''
Дан граф в виде списка вершин. Необходимо понять, есть ли
в этом графе цикл
'''

def has_cycle(graph):
    visited = set()

    for vertex in graph:
        if vertex not in visited:
            if dfs(graph, vertex, None, visited):
                return True
    return False


def dfs(graph, vertex, parent, visited):
    visited.add(vertex)

    for neighbor in graph[vertex]:
        if neighbor != parent:
            if neighbor in visited or dfs(graph, neighbor, vertex, visited):
                return True
    return False
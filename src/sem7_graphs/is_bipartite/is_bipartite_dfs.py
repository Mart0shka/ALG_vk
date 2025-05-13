def is_bipartite_dfs(graph):
    colors = {}

    def dfs(node, color):
        colors[node] = color
        for neighbor in graph[node]:
            if neighbor not in colors:
                if not dfs(neighbor, -color):
                    return False
            elif colors[neighbor] == color:
                return False
        return True

    for node in graph:
        if node not in colors:
            if not dfs(node, 1):
                return False
    return True

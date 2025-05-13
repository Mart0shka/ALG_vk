from collections import deque

def is_bipartite_bfs(graph):
    colors = {}

    for start in graph:
        if start not in colors:
            queue = deque([start])
            colors[start] = 1

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in colors:
                        colors[neighbor] = -colors[node]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False
    return True

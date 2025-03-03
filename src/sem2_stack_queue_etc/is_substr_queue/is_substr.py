from collections import deque

"""
В исходную строку добавили некоторое количество символов. Необходимо выявить, была ли строка a исходной для строки b.
"""

def is_substr(a, b):
    q = deque()
    for elem in a:
        q.append(elem)
    for elem in b:
        if q and elem == q[0]:
            q.popleft()
    return len(q)==0
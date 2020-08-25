import sys
from collections import deque

visited = []
qy = deque()
n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
    u, m = map(int, input().split())
    graph[u].append(m)
    graph[m].append(u)


def dfs(start):
    for i in range(n):
        graph[i].sort()
    qy.append(start)
    if graph[start]:

        while qy:
            y = qy.popleft()
            if y not in visited:
                visited.append(y)
                for i in graph[y]:
                    if i not in visited:
                        qy.append(i)


count = 0
for i in range(1, n + 1):
    if i not in visited:
        dfs(i)
        count += 1

print(count)
""" 아래 코드는 왜 안되는지 모르겠음
import sys
from collections import deque

visited = []
qy = deque()
n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
for i in range(m):
    u, m = map(int, input().split())
    graph[u].append(m)
    graph[m].append(u)


def bfs():
    count = 0
    for i in range(len(graph)):
        if i not in visited:
            if (graph[i]):
                visited.append(i)
                qy.append(i)
                count = count + 1
                while (qy):
                    y = qy.popleft()
                    visited.sort(reverse=True)
                    for child in graph[y]:
                        if child not in visited:
                            visited.append(child)
                            qy.append(child)

    return count


print(bfs())
"""
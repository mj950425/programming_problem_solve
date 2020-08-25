from collections import deque

N, M = map(int, input().split())
graph = [[] for i in range(N + 1)]
graphh = [[] for i in range(N + 1)]
visited = [False * N + 1]
for i in range(M):
    u, m = map(int, input().split())
    # u가 m보다 무겁다는것을 뜻함
    graph[u].append(m)
    graphh[m].append(u)
# DFS로 이어진게 (N+1)/2 개 이면 절반
# 그래프를 두개 만들어서 작은거 큰거 기준에서 각각 DFS를 실시

ans = []
count = 0


def dfs(start):
    global count
    count += 1
    if count > (N + 1) / 2:
        ans.append(start)
        return
    for _ in graph[start]:
        visited[_] = True
        dfs(_)

    return


def ddfs(start):
    global count
    count += 1
    if count > (N + 1) / 2:
        ans.append(start)
        return
    ddfs(graph[start])
    return


for start in range(M + 1):
    dfs(start)
    count = 0
    ddfs(start)


def ddfs(start):
    global count
    count+=1
    if count>(N+1)/2:
        ans.append(start)
        return
    ddfs(graph[start])
    return


for start in range(M+1):
    dfs(start)
    count=0
    ddfs(start)


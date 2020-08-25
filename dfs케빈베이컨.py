import sys
from collections import deque

N,M= map(int,sys.stdin.readline().split())

graph=[[] for i in range(N+1)]
for i in range(M):
    u,m= map(int,sys.stdin.readline().split())
    graph[u].append(m)
    graph[m].append(u)


all=[]
def bfs(start,c):
    q = deque()
    qc = deque()
    visited = [0 for i in range(N + 1)]
    sum=0
    visited[start]=1
    q.append(start)
    qc.append(1)
    while(q):
        c = qc.popleft()
        x =  q.popleft()
        sum=sum+c
        for i in graph[x]:
            if visited[i] == 0:
                q.append(i)
                visited[i]=1
                qc.append(c + 1)

    all.append(sum)

for i in range(1,N+1):
    bfs(i,1)
for i in range(N):
    if all[i]==min(all):
        print(i+1)
        break



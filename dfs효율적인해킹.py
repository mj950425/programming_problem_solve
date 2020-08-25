"""
https://www.acmicpc.net/problem/1325



import sys
from collections import deque
N,M=map(int,sys.stdin.readline().split())
graph=[[] for i in range(N+1)]
for i in range(M):
    u,m=map(int,sys.stdin.readline().split())
    graph[m].append(u)
print(graph)
visited=[0 for i in range(N)]

def dfs(start):
    global count
    visited[start]=1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            count=count+1
        else:
            return False


for i in range(N):
    if visited[i]==0:
        count = 0
        dfs(i)
        print("i,count",i,count)

"""
import sys
N,M=map(int,sys.stdin.readline().split())
graph=[[] for i in range(N+1)]
for i in range(M):
    u,m=map(int,sys.stdin.readline().split())
    graph[m].append(u)

def dfs(start):
    global count
    visited[start]=1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            count=count+1
        else:
            return False

buf=0
answer=[]
for i in range(1,N):
    visited=[0 for k in range(N+1)]
    count = 0
    dfs(i)
    if buf == count:
        answer.append(i)
    if buf < count:
        buf=count
        answer=[]
        answer.append(i)
for _ in answer:
    print(_,end=' ')

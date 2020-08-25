"""

https://www.acmicpc.net/status?user_id=minjoon1324&problem_id=1707&from_mine=1


if not dfs(i,-c)로 조건문에 걸어줘도 dfs를 방문한다.!!!!!!!!
"""
import sys
sys.setrecursionlimit(100000)

def dfs(start,c):
    visited[start]=c
    for i in graph[start]:
        if visited[i]==0:
            if not dfs(i,-c):
                return False
        elif visited[i]==visited[start]:
            return False
    return True





case=int(input())
for i in range(case):
    V,E= map(int,sys.stdin.readline().split())
    graph=[[] for i in range(V+1)]
    for i in range(E):
        u,m=map(int,sys.stdin.readline().split())
        graph[u].append(m)
        graph[m].append(u)
    visited=[0 for i in range(V+1)]
    ans=True
    for i in range(1,V+1):
        if visited[i]==0:
            if not dfs(i,1):
                ans= False
                break
    if ans == True:
        print("YES")
    else:
        print("NO")




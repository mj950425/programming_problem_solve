"""
ㅗ 모양을 새롭게 구현해주어야했다....!!!! ㅠㅠㅠ
브루트포스로 풀자
"""
from collections import deque
N,M=list(map(int,input().split()))
graph=[]
for i in range(N):
    graph.append(list(map(int,input().split())))
visited=[[0 for i in range(M)] for i in range(N)]
dx=[0,0,-1,1]
dy=[-1,1,0,0]
qx=deque()
qy=deque()
answer=0
def dfs(y,x):
    global num,count,max
    num += 1
    count += graph[y][x]
    visited[y][x] = 1

    if num==4:
        if max < count:
            max = count
        num -= 1
        visited[y][x] = 0
        count -= graph[y][x]

        return

    for i in range(4):
        Y=y+dy[i]
        X=x+dx[i]
        if 0 <= Y and Y < N and 0<= X and X < M:
            if visited[Y][X] != 1:
                dfs(Y,X)

    visited[y][x]=0
    num-=1
    count -= graph[y][x]

    return max




max=0
for i in range(N):
    for j in range(M):
        num=0
        count=0

        dfs(i,j)

        if answer<max:
            answer=max
print(answer)


# 0: 위 1: 오른쪽 2: 아래 3: 왼쪽
from collections import deque
N,M=list(map(int,input().split()))
y,x,d=list(map(int,input().split()))
graph=[]
for i in range(N):
    graph.append(list(map(int,input().split())))
visited=[[False * M]*N]
qx=deque()
qy=deque()

dx=[-1,0,1,0]
dy=[0,-1,0,1]

bx=[0,-1,0,+1]
by=[+1,0,-1,0]
count = 0


def check(y,x):
    if y>N-1 or y<0 or x>M-1 or x<0:
        return False
    if graph[y][x]!=0:
        return False
    return True

def bfs(y,x,d):
    qq=0
    buf=0
    global count
    qx.append(x)
    qy.append(y)
    while(1):
        x=qx.popleft()
        y=qy.popleft()

        if graph[y][x]==0:
            count += 1
        graph[y][x]=2



        for i in range(4):
            Y = y + dy[d]
            X = x + dx[d]
            if check(Y,X):

                qy.append(Y)
                qx.append(X)
                d = (d + 3) % 4
                break
            else:
                d = (d + 3) % 4

            if i ==3:
                buf=1

        if buf==1:
            if graph[y+by[d]][x+bx[d]]==1:

                return
            else:
                qx.append(x+bx[d])
                qy.append(y+by[d])
                buf=0


bfs(y,x,d)
print(count)


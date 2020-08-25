from collections import deque

qx = deque()
qy = deque()
N = int(input())
arr = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(N):
    arr.append(list(map(int, list(input().split()))))


def check(y,x,visited):
    if x < 0 or x > N - 1 or y < 0 or y > N - 1:
        return False
    if arr[y][x] == 0:

        return False

    if visited[y][x] == 1:

        return False

    return True

def dis():
    com=0
    answer=50000
    for i in range(N):
        for j in range(N):
            if arr[i][j] !=0:
                com=arr[i][j]
                for q in range(N):
                    for w in range(N):
                        if arr[q][w] !=0 and arr[q][w] != com :
                            ans=abs(i-q)+abs(j-w)
                            if answer > ans :
                                answer= ans
    print(answer-1)

def bfs():
    buf = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and arr[i][j] != 0:
                buf = buf + 1
                arr[i][j] = buf

                qy.append(i)
                qx.append(j)
                while qy:
                    xx = qx.popleft()
                    yy = qy.popleft()
                    for k in range(4):
                        x = xx + dx[k]
                        y = yy + dy[k]
                        if check(y, x,visited):
                            qx.append(x)
                            qy.append(y)
                            arr[y][x] = buf
                            visited[y][x] = 1


bfs()
dis()
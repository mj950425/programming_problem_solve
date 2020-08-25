"""
https://www.acmicpc.net/problem/2573
"""
from collections import deque

qx = deque()
qy = deque()
N, M = map(int, input().split())
ar = [0 for i in range(M)]
arr = []
count = 0
num = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(N):
    arr.append(list(map(int, list(input().split()))))


def check(y, x,visited):
    if x < 0 or x > M - 1 or y < 0 or y > N - 1:
        return False

    if arr[y][x] == 0:
        return False
    if visited[y][x]==1:
        return False

    return True


breaker = False


def bfs():
    count = 0
    buf = 0
    global breaker
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if count == 2:
                return False

            if visited[i][j] == 0 and arr[i][j] != 0:

                count = count + 1
                qy.append(i)
                qx.append(j)
                while qy:
                    xx = qx.popleft()
                    yy = qy.popleft()
                    for _ in range(4):
                        x = xx + dx[_]
                        y = yy + dy[_]
                        if check(y, x,visited):

                            qx.append(x)
                            qy.append(y)
                            visited[y][x] = 1
    return True

def meltingcnt():
    meltarr = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                meltcnt = 0
                for k in range(4):
                    if arr[i + dy[k]][j + dx[k]] == 0:
                        meltcnt = meltcnt + 1

                meltarr[i][j] = meltcnt

    for i in range(N):
        for j in range(M):
            arr[i][j] = arr[i][j] - meltarr[i][j]
            if arr[i][j] < 0:
                arr[i][j] = 0



def check_ice():
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0:
                return True
    return False


year = 0

while bfs():
    if not check_ice():
        year = 0
        break
    year += 1
    meltingcnt()

print(year)



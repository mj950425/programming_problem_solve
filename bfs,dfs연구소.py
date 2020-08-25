from collections import deque

qx=deque()
qy=deque()
candi = 0
put = []
N, M = map(int, input().split())

for _ in range(N):
    put.append(list(map(int, list(input().split()))))

backup = put

ret = 0


def bfs(y, x):
    for i in range(N):
        for j in range(M):
            if (put[i][j] == 2):
                qx.append(j)
                qy.append(i)
    while (qy):
        xx = qx.popleft()
        yy = qy.popleft()

        # 상
        if (put[yy - 1][xx] != 0 or y > N - 1 or y < 0 or x > M - 1 or x < 0):
            qy.append(yy - 1), qx.append(xx)

        # 하
        if (put[yy - 1][xx] != 0 or y > N - 1 or y < 0 or x > M - 1 or x < 0):
            qy.append(yy + 1), qx.append(xx)

        # 좌
        if (put[yy][xx - 1] != 0 or y > N - 1 or y < 0 or x > M - 1 or x < 0):
            qy.append(yy), qx.append(xx - 1)

        # 우
        if (put[yy][xx + 1] != 0 or y > N - 1 or y < 0 or x > M - 1 or x < 0):
            qy.append(yy), qx.append(xx + 1)
    candi = 0

    for i in range(N):
        for j in range(M):
            if (put[i][j] == 0):
                candi = candi + 1

    if (ret < candi):
        ret = candi

    return ret


def dfs(count, pos_x, pos_y):
    if (count == M):
        bfs()
        return
    for i in range(pos_y, N + 1):
        for j in range(pos_x, M + 1):
            if (put[i][j] == 0):
                put[i][j] = 1
                dfs(count + 1, pos_y, pos_x + 1)
                put[i][j] = 0

        pos_x = 0


dfs(0, 0)
print(ret)



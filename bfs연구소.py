from collections import deque

qx = deque()
qy = deque()
candi = 0
ret = 0
put = []
virus = []
N, M = map(int, input().split())
for i in range(N):
    put.append(list(map(int, list(input().split()))))
    for j in range(M):
        if (put[i][j] == 2):
            virus.append((i, j))


def check(x, y, putt):
    if (y > N - 1 or y < 0 or x > M - 1 or x < 0):
        return False

    if (putt[y][x] != 0):
        return False

    return True


def bfs(putt):
    global ret

    for (i, j) in virus:
        q = [(i, j)]
        qx.append(j)
        qy.append(i)

    while (qy):

        xx = qx.popleft()
        yy = qy.popleft()

        # 상
        if (check(xx, yy - 1, putt)):
            qy.append(yy - 1), qx.append(xx)
            putt[yy - 1][xx] = 2
        # 하
        if (check(xx, yy + 1, putt)):
            qy.append(yy + 1), qx.append(xx)
            putt[yy + 1][xx] = 2
        # 좌
        if (check(xx - 1, yy, putt)):
            qy.append(yy), qx.append(xx - 1)
            putt[yy][xx - 1] = 2
        # 우
        if (check(xx + 1, yy, putt)):
            qy.append(yy), qx.append(xx + 1)
            putt[yy][xx + 1] = 2

    candi = 0

    for i in range(N):
        for j in range(M):
            if (putt[i][j] == 0):
                candi = candi + 1

    if (ret < candi):
        ret = candi

    return ret


def dfs(count, pos_y, pos_x):
    if (count == 3):
        putt = [[0 for _ in range(M)] for _ in range(N)]

        for i in range(N):
            for j in range(M):
                if put[i][j] != 0:
                    putt[i][j] = put[i][j]

        bfs(putt)

        return
    for i in range(pos_y, N):
        for j in range(pos_x, M):
            if (put[i][j] == 0):
                put[i][j] = 1
                dfs(count + 1, i, j + 1)
                put[i][j] = 0

        pos_x = 0


dfs(0, 0, 0)
print(ret)




from collections import deque
put=[]
backup=[]
buff=0
buf = 0
qx = deque()
qy = deque()
N = int(input())
for i in range(N):
    put.append(list(map(int, list(input().split()))))
q = set(sum(put, []))

for i in range(N):
    backup.append([])
    for j in range(N):
        backup[i].append(0)

for i in range(N):
    for j in range(N):
        backup[i][j]=put[i][j]





def check(yy, xx):
    if (yy > N-1 or yy < 0 or xx > N-1 or xx < 0):
        return False
    if (put[yy][xx] == 0):
        return False
    return True


for rain in q:

    if(buf>buff):
        buff=buf
    buf=0
    for i in range(N):
        for j in range(N):
            put[i][j]=backup[i][j]
            if (put[i][j] <= rain):
                put[i][j] = 0


    for i in range(N):
        for j in range(N):
            if (put[i][j] != 0):
                qx.append(j)
                qy.append(i)
                buf = buf + 1


                while (qy):
                    yy = qy.popleft()
                    xx = qx.popleft()
                    put[yy][xx] = 0
                    # 상
                    if (check(yy - 1, xx)):
                        put[yy - 1][xx] = 0
                        qy.append(yy - 1), qx.append(xx)
                    # 하
                    if (check(yy + 1, xx)):
                        put[yy + 1][xx] = 0

                        qy.append(yy + 1), qx.append(xx)
                    # 좌
                    if (check(yy, xx - 1)):
                        put[yy][xx - 1] = 0
                        qy.append(yy), qx.append(xx - 1)
                    # 우
                    if (check(yy, xx + 1)):
                        put[yy][xx + 1] = 0
                        qy.append(yy), qx.append(xx + 1)


if(buff==0):
    print(1)
else:
    print(buff)
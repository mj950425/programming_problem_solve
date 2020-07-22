"""
http://localhost:8888/notebooks/Untitled1.ipynb

배열 크기와 방문 여부를 확인하는 check 함수를 만들어서 구현하면 시간이 오래걸린다.
파이썬은 함수 호출이 시간이 오래걸린다.
"""
from collections import deque

put = []
mp = []
buff = []
buf = 1
cnt = 1
qx = deque()
qy = deque()
M, N, K = map(int, input().split())
for i in range(K):
    put.append(list(map(int, list(input().split()))))

for i in range(N):
    mp.append([])
    for j in range(M):
        mp[i].append(0)

for w in range(K):
    for i in range(put[w][0], put[w][2]):
        for j in range(put[w][1], put[w][3]):
            mp[i][j] = 1

for i in range(N):
    for j in range(M):
        if (mp[i][j] == 0):
            qy.append(i)
            qx.append(j)
            buf = buf + 1
            mp[i][j] = buf
            cnt = 1
            while (qy):
                yy = qy.popleft()
                xx = qx.popleft()

                # 상
                if (yy - 1 < N and yy - 1 >= 0 and xx < M and xx >= 0):
                    if (mp[yy - 1][xx] == 0):
                        mp[yy - 1][xx] = buf
                        qy.append(yy - 1)
                        qx.append(xx)
                        cnt = cnt + 1

                # 하
                if (yy + 1 < N and yy + 1 >= 0 and xx < M and xx >= 0):
                    if (mp[yy + 1][xx] == 0):
                        mp[yy + 1][xx] = buf
                        qy.append(yy + 1)
                        qx.append(xx)
                        cnt = cnt + 1
                # 좌
                if (yy < N and yy >= 0 and xx - 1 < M and xx - 1 >= 0):
                    if (mp[yy][xx - 1] == 0):
                        mp[yy][xx - 1] = buf
                        qy.append(yy)
                        qx.append(xx - 1)
                        cnt = cnt + 1
                # 우
                if (yy < N and yy >= 0 and xx + 1 < M and xx + 1 >= 0):
                    if (mp[yy][xx + 1] == 0):
                        mp[yy][xx + 1] = buf
                        qy.append(yy)
                        qx.append(xx + 1)
                        cnt = cnt + 1
            buff.append(cnt)
buff.sort()
buf = buf - 1
print(buf)
for i in buff:
    print(i, end=' ')

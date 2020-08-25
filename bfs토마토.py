"""
https://www.acmicpc.net/problem/7576

창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다.
보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다.
대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다.
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라.
단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다.
단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다.
즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다.
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

예제 입력
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

예제 출력
8

"""
from collections import deque

put = []
visited = []
qx = deque()
qy = deque()
qc = deque()
cnt = 0
N, M = map(int, input().split())
for _ in range(N):
    put.append(list(map(int, list(input().split()))))


def check(yy, xx):
    if (yy < 0 or yy > N - 1 or xx < 0 or xx > M - 1):
        return False
    if (put[yy][xx] == 1):
        return False
    if (put[yy][xx] == -1):
        return False

    return True


for i in range(N):
    for j in range(M):
        if (put[i][j] == 1):
            qy.append(i), qx.append(j), qc.append(0)

while (qy):
    xx = qx.popleft()
    yy = qy.popleft()
    cc = qc.popleft()

    # 상
    if (check(yy - 1, xx)):
        qx.append(xx)
        qy.append(yy - 1)
        qc.append(cc + 1)
        put[yy - 1][xx] = 1
    # 하
    if (check(yy + 1, xx)):
        qx.append(xx)
        qy.append(yy + 1)
        qc.append(cc + 1)
        put[yy + 1][xx] = 1

    # 좌
    if (check(yy, xx - 1)):
        qx.append(xx - 1)
        qy.append(yy)
        qc.append(cc + 1)
        put[yy][xx - 1] = 1

    # 우
    if (check(yy, xx + 1)):
        qx.append(xx + 1)
        qy.append(yy)
        qc.append(cc + 1)
        put[yy][xx + 1] = 1

print(cc)
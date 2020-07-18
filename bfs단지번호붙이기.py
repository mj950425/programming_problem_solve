"""
백준 알고리즘 2667번
https://www.acmicpc.net/problem/2667

정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
대각선상에 집이 있는 경우는 연결된 것이 아니다.
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

예제 입력
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

예제 출력
3
7
8
9

"""
from collections import deque

put = []
visited = []
count = []
qx = deque()
qy = deque()
qc = deque()
cnt = 0
buf = 1
N = int(input())
put = [[int(x) for x in input()] for y in range(N)]


def check(x, y):
    if (y > N - 1 or y < 0 or x > N - 1 or x < 0):
        return False
    if (put[y][x] != 1):
        return False

    return True


for i in range(N):
    for j in range(N):
        if (put[i][j] == 1):
            qy.append(i), qx.append(j), qc.append(1)
            buf = buf + 1
            cnt = 1
            while (qy):
                xx = qx.popleft()
                yy = qy.popleft()
                cc = qc.popleft()
                put[yy][xx]=buf
                # 상
                if (check(xx, yy - 1)):
                    put[yy - 1][xx] = buf
                    qx.append(xx + 0), qy.append(yy - 1), qc.append(cc + 1)
                    cnt = cnt + 1
                # 하
                if (check(xx, yy + 1)):
                    put[yy + 1][xx] = buf
                    qx.append(xx + 0), qy.append(yy + 1), qc.append(cc + 1)
                    cnt = cnt + 1
                # 좌
                if (check(xx - 1, yy)):
                    put[yy][xx - 1] = buf
                    qx.append(xx - 1), qy.append(yy + 0), qc.append(cc + 1)
                    cnt = cnt + 1
                # 우
                if (check(xx + 1, yy)):
                    put[yy][xx + 1] = buf
                    qx.append(xx + 1), qy.append(yy + 0), qc.append(cc + 1)
                    cnt = cnt + 1

            count.append(cnt)
buf = buf - 1
print(buf)
count.sort()
for i in list(count):
    print(i)
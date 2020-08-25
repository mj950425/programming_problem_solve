"""
백준 알고리즘 1697번
https://www.acmicpc.net/problem/1697

수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

예제 입력
5 17

예제 출력
4
"""
from collections import deque

M, N = map(int, input().split())
qx = deque()
qc = deque()
qx.append(M)
qc.append(0)
visited = [False] * 10001000


def check(xx):
    if (visited[xx] == True):
        return False
    return True


while (qx):
    xx = qx.popleft()
    cc = qc.popleft()
    if (xx == N):
        cnt = cc
        break
    # xx+1
    if (xx < N):
        if (check(xx + 1)):
            qx.append(xx + 1)
            qc.append(cc + 1)
            visited[xx + 1] = True
    # xx-1
    if (check(xx - 1)):
        qx.append(xx - 1)
        qc.append(cc + 1)
        visited[xx - 1] = True

    # xx*2
    if (xx < N):
        if (check(xx * 2)):
            qx.append(xx * 2)
            qc.append(cc + 1)
            visited[xx * 2] = True

print(cnt)

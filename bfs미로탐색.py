"""
https://www.acmicpc.net/problem/2178

N×M크기의 배열로 표현되는 미로가 있다.
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

예제 입력
4 6
101111
101010
101011
111011

예제 출력
15

"""
from collections import deque

put=[]
visited=[]
qx= deque()
qy= deque()
qc= deque()
cnt =0
N,M =map(int,input().split())

for _ in range(N):
    put.append(list(map(int, list(input()))))

#depth = [[0 for j in range(M)] for k in range(M)]

qy.append(0),qx.append(0),qc.append(1)
def check( x, y):
    if (y>N-1 or y<0 or x>M-1 or x<0):
        return False
    if (put[y][x] ==0):
        return False

    return True

while(qy):

    xx = qx.popleft()
    yy = qy.popleft()
    cc = qc.popleft()
    put[yy][xx] = 0
    if (xx==M-1 and yy==N-1):
        cnt=cc
        break

    #상
    if(check(xx,yy-1)):
        put[yy-1][xx] = 0
        qx.append(xx+0),qy.append(yy-1),qc.append(cc+1)
    #하
    if(check(xx,yy+1)):
        put[yy+1][xx] = 0
        qx.append(xx+0),qy.append(yy+1),qc.append(cc+1)
    #좌
    if(check(xx-1,yy)):
        put[yy][xx-1] = 0
        qx.append(xx-1),qy.append(yy+0),qc.append(cc+1)
    #우
    if(check(xx+1,yy)):
        put[yy][xx+1] = 0
        qx.append(xx+1),qy.append(yy+0),qc.append(cc+1)


print(cnt)


"""
import sys
sys.setrecursionlimit(99999)
import queue

N,M =map(int,input().split())

for _ in range(N):
    map_.append(list(map(int, list(input()))))

q = queue.Queue()
dx_dy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
chk = [[False for y in range(M)] for x in range(N)]

def chk_in_map(x, y, n, m):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False

ans = []

def bfs(x, y, chk, cnt):
    chk[x][y] = True
    cnt += 1
    for diff in dx_dy:
        ax, ay = [sum(z) for z in zip((x, y), diff)]
        if chk_in_map(ax, ay, len(chk), len(chk[0])):
            if map_[ax][ay] == 1 and chk[ax][ay] == False:
                chk[ax][ay] = True
                if ax == len(chk)-1 and ay == len(chk[0])-1:
                    ans.append(cnt)
                q.put((ax, ay, cnt))
    if q.qsize() != 0:
        ax, ay, cnt = q.get()
        bfs(ax, ay, chk, cnt)
    return ans

print(min(bfs(0, 0, chk, 1)))

"""
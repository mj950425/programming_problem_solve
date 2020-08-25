"""
백준 알고리즘 1012번
https://www.acmicpc.net/problem/1012
이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다.
특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다.
(한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있다고 간주한다)
한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어놓았다.
배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.

예제 입력
1
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0

예제 출력
2

"""
from collections import deque
qx=deque()
qy=deque()
qc=deque()
cnt=[]
put=[]
num = int(input())
#농장의 개수를 입력받는다
for _ in range(num):
    buf=1
    M,N,k =map(int,input().split())
    farm = [[0 for j in range(M)] for k in range(N)]
    #양배추의 좌표를 입력 받고 farm에 1로 표시해준다
    for _ in range(k):
        put=map(int, list(input().split()))
        put=list(put)
        farm[put[1]][put[0]]=1
    def check(y,x):
        if(y>N-1 or y<0 or x>M-1 or x<0):
            return False
        if(farm[y][x]!=1):
            return False
        return True

#for문 2개로 양배추가 있는 위치를 찾아낸다
    for i in range(N):
        for j in range(M):
            #찾아내면 bfs 완전 탐색으로 붙어있는 아파트 단지를 전부 buf로 바꿔준다
            if (farm[i][j]==1):
                buf=buf+1
                qx.append(j)
                qy.append(i)
                while(qy):
                    xx = qx.popleft()
                    yy = qy.popleft()

                    farm[yy][xx]=buf

                    #상
                    if(check(yy -1,xx)):
                        qx.append(xx)
                        qy.append(yy-1)

                        farm[yy-1][xx]=buf
                    #하
                    if(check(yy +1,xx)):
                        qx.append(xx)
                        qy.append(yy+1)
                        farm[yy-1][xx]=buf
                    #좌
                    if(check(yy,xx-1)):
                        qx.append(xx-1)
                        qy.append(yy)
                        farm[yy-1][xx]=buf
                    #우
                    if(check(yy,xx+1)):
                        qx.append(xx+1)
                        qy.append(yy)
                        farm[yy-1][xx]=buf

    cnt.append(buf-1)
for i in list(cnt):
    print(i)
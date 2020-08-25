from collections import deque
stack=deque()
put=[]
count=[]
R, C = map(int, input().split())
for i in range(R):
    put.append(list(map(str,list(input()))))
print("aaaaaa")
visited_Alpha = [0 for _ in range(26)]
visited_Alpha[ord(put[0][0])-65] = 1
visited = [[0 for _ in range(C)] for __ in range(R)]
visited[0][0]=1
dx=[0,0,-1,1]
dy=[1,-1,0,0]
def check(yy,xx):
    if(yy<0 or yy>R-1 or xx<0 or xx>C-1):
        return False
    if (visited_Alpha[ord(put[yy][xx])-65]==1):
        return False
    if (visited[yy][xx]==1) :
        return False
    return True

def dfs(y,x,c):
    count.append(c)
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]

        if check(yy,xx):
            visited[yy][xx]=1
            visited_Alpha[ord(put[yy][xx])-65]=1
            dfs(yy,xx,c+1)

            visited[yy][xx]=0
            visited_Alpha[ord(put[yy][xx])-65]=0
print("start")
dfs(0,0,0)
print(max(count))
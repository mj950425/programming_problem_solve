from collections import deque
qy=deque()
qx=deque()
dx=[0,0,-1,1]
dy=[-1,1,0,0]
put=[]
c=0
N= int(input())
backup=[[ 0 for _ in range(N)] for __ in range(N)]
for i in range(N):
    put.append(list(map(str,list(input()))))

def check(yy,xx,buf,put):
    if yy>N-1 or yy<0 or xx>N-1 or xx<0:
        return False
    if put[yy][xx]!=buf:
        return False
    return True


    return True
def bfs():
    for i in range(N):
        for j in range(N):
            backup[i][j]=put[i][j]
            if backup[i][j]=="R":
                backup[i][j]="G"
    num = 0

    for i in range(N):
        for j in range(N):
            print("i,j",i,j)
            if put[i][j]=="R" or put[i][j]=="G" or put[i][j]=="B":
                num=num+1
                qx.append(j)
                qy.append(i)
                buf=put[i][j]
                put[i][j]=num
                while(qy):
                    xx=qx.popleft()
                    yy=qy.popleft()
                    for z in range(4):
                        temp_x=xx+dx[z]
                        temp_y=yy+dy[z]
                        if check(temp_y,temp_x,buf,put):
                            put[temp_y][temp_x]=num
                            qx.append(temp_x)
                            qy.append(temp_y)
    num1 = 0

    for i in range(N):
        for j in range(N):
            if  backup[i][j]=="G" or backup[i][j]=="B":
                num1=num1+1
                qx.append(j)
                qy.append(i)
                buf=backup[i][j]
                backup[i][j]=num1
                while(qy):
                    xx=qx.popleft()
                    yy=qy.popleft()
                    for z in range(4):
                        temp_x=xx+dx[z]
                        temp_y=yy+dy[z]
                        if check(temp_y,temp_x,buf,backup):
                            backup[temp_y][temp_x]=num1
                            qx.append(temp_x)
                            qy.append(temp_y)
    print(num,num1)

bfs()

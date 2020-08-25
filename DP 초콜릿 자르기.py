N,M=list(map(int,input().split()))
arr=[[0]*(M+1) for i in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        arr[i][j]=j*(i)-1
print(arr[N][M])
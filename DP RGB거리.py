N= int(input())
arr=[]
a=[]
for i in range(N):
    arr.append(list(map(int,input().split())))
    a.append([0,0,0])
for i in range(1,N):
    arr[i][0]=arr[i][0]+min(arr[i-1][1],arr[i-1][2])
    arr[i][1]=arr[i][1]+min(arr[i-1][0],arr[i-1][2])
    arr[i][2]=arr[i][2]+min(arr[i-1][0],arr[i-1][1])
print(min(arr[N-1]))


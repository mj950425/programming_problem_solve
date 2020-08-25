case=int(input())
for j in range(case):
    N=int(input())
    lst=[0 for i in range(N)]
    lst[0]=1
    lst[1]=1
    lst[2]=1
    lst[3]=2
    lst[4]=2
    for i in range(N):
        lst[i]=lst[i-5]+lst[i-1]
    print(lst[N-1])
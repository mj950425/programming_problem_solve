N=int(input())
lst=list(map(int,input().split()))
dp=[0 for i in range(N+1)]
dp[0]=lst[0]

for i in range(1,N):
    a=[0]+[lst[i]]
    for j in range(i):
        if lst[i] > lst[j]:
            a = a+[dp[j]+lst[i]]
    dp[i]=max(a)

print(max(dp))

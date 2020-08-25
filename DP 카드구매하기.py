N=int(input())
arr=list(map(int,input().split()))
arr=[0]+arr
dp=[0 for i in range(N)]
dp=[0]+dp
dp[1]=arr[1]
buf=0
for i in range(2,N+1):
    for j in range(i):
        dp[i] = max(buf,dp[i-j]+arr[j],dp[i-j-1]+arr[j+1])
        buf=dp[i]
print(dp[N])

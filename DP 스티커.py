answer=[]
case=int(input())
for i in range(case):
    n=int(input())
    a=[list(map(int,input().split()))]
    a.append(list(map(int,input().split())))
    dp=[[0] * n for i in range(2)]
    dp[0][0]=a[0][0]
    dp[1][0]=a[1][0]
    dp[0][1]=max(dp[1][0]+a[0][1],dp[0][0])
    dp[1][1]=max(dp[0][0]+a[1][1],dp[1][0])
    for j in range(2, n):
        for i in range(2):
            dp[i][j]=max(dp[1-i][j-1]+a[i][j],dp[1-i][j-2],dp[i][j-1])
    m=0
    for i in range(2):
        if m < max(dp[i]):
            m=max(dp[i])
    answer=answer+[m]
for i in answer:
    print(i)

n, m = map(int, input().split())
dp = [0 for i in range(m+1)]
lst = []
dp[0]=1
for i in range(n):
    lst.append(int(input()))

for i in lst:
    for j in range(i,m+1):
        if j-i>=0:
            dp[j] += dp[j-i]
print(dp[m])

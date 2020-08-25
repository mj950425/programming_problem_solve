N = int(input())
lst = list(map(int, input().split()))
dp=[0 for i in range(N)]
for i in range(N):
    a = [0]
    for j in range(i):
        if lst[i] > lst[j]:
            a = a + [dp[j] + lst[j]]

    dp[i] = max(a)
print(max(dp))


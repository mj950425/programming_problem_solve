
def solution():
    count=0
    N = int(input())
    for _ in range(1,10):
        dp = [[0] * 10 for i in range(N)]
        dp[0][_]=1

        for i in range(1,N):
            for j in range(10):
                if dp[i-1][j] != 0:
                    if j ==0:
                        dp[i][1] += dp[i-1][0]
                    elif j== 9:
                        dp[i][8] += dp[i-1][9]
                    else:
                        dp[i][j+1] += dp[i-1][j]
                        dp[i][j-1] += dp[i-1][j]
            if i==1:
                print(dp)
        for i in range(10):
            count=count+dp[N-1][i]


    return count%1000000000000000000000000000000000000

print(solution())
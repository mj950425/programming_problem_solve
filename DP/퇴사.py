"""
-----------------------------
Level : 1
-----------------------------
Problem : 
매일 새로운 일이 가치와 소요 시간과 함께 주어질 때, 
가치를 최대로 만드는 문제.
------------------------------
input :
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
-----------------------------
output : 
45
-----------------------------
problem link : https://www.acmicpc.net/problem/14501
-----------------------------
"""

n = int(input())
T, P = [0 for i in range(n+1)], [0 for i in range(n+1)]

for i in range(n):
    a,b = map(int, input().split())
    T[i] = a
    P[i] = b

dp =[0 for i in range(n+1)]

for i in range(len(T)-2, -1, -1):
    if T[i]+i <= n:
        dp[i] = max(P[i]+dp[i+T[i]], dp[i+1])
    else:
        dp[i] = dp[i+1]
print(dp[0])
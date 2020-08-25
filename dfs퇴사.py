
"""
https://www.acmicpc.net/problem/14501

"""
N=int(input())
graph=[[] for i in range(N+1)]

for i in range(1,N+1):
    u,m=list(map(int,input().split()))
    graph[i]=graph[i]+[u,m]
arr=[[] for i in range(N+1)]

for i in range(1,N+1):
    arr[i]=arr[i]+[j for j in range(i+graph[i][0],N+1)]
    if (i+graph[i][0])==N+1:
        arr[i]=[0]
answer = []

def dfs(start,count):
    global buf

    if arr[start]:
        count=count+graph[start][1]
        for i in arr[start]:
            dfs(i,count)

    else:
        answer.append(count)

        return
for i in range(1,N+1):

    dfs(i,0)
print(max(answer))

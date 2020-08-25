N=int(input())
graph=[]
for i in range(N):
    graph.append(list(map(int,input().split())))




for i in range(1,N):
    for j in range(i+1):

        if j == 0:
            graph[i][j]=graph[i][j]+graph[i-1][j]
        elif j == i:
            graph[i][j]=graph[i][j]+graph[i-1][j-1]
        else:
            graph[i][j]=graph[i][j]+max(graph[i-1][j],graph[i-1][j-1])

print(max(graph[N-1]))

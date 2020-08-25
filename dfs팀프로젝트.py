import sys
sys.setrecursionlimit(200000)


def dfs(start):
    if visited[start]==1 and put[start] != buf:
        return
    visited[start]=1
    if put[start] ==buf :
        for _ in range(N+1):
            if visited[_]==1:
                answer[_]=1
        return answer
    dfs(put[start])
    return

a=[]
case = int(input())
for ___ in range(case):
    buf=0
    N = int(sys.stdin.readline())
    put = list(map(int, list(sys.stdin.readline().split())))
    put=[[]]+put
    answer=[1]+[0 for i in range(N)]
    count=0
    for start in range(1,N+1):
        visited=[0 for i in range(N+1)]
        buf=start
        dfs(start)
    for i in range(N+1):
        if answer[i]==0:
            count += 1
    a.append(count)
for i in a:
    print(i,end=' ')

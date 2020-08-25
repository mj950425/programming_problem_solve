from collections import deque
stack=deque()
answer=[]
num=0
N=int(input())
graph=[0 for i in range(N+1)]

" graph를 만들어줌 <--- 첫번째 원소는 비어있음"
for i in range(N):
    u=int(input())
    graph[i]=u
graph=[0]+graph

"dfs로 조합 구현"


def dfs(x):
    global num
    global N
    global answer
    if len(stack) == i:
        arr=[]
        for s in stack:
            arr=arr+[graph[s]]
            arr.sort()
            if arr==list(stack):
                if len(arr)>len(answer):
                    answer=arr
                    num=i

        return

    for j in range(x, N + 1):
        stack.append(x)
        dfs(j + 1)
        stack.pop()


"몇개뽑을지 결정"
for i in range(N+1):
    count = 0
    dfs(1)
print(num)
for i in answer:
    print(i)


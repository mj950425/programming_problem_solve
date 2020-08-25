"""

from collections import deque
N=int(input())
q=deque()
c=deque()
q.append(1)
c.append(1)
def bfs():
    answer=0
    while(True):
        x = q.popleft()
        cnt=c.popleft()
        if cnt==N:
            answer += 1
        if cnt==N+1:
            return answer
        if x==1:
            q.append(0)
            c.append(cnt+1)
        if x==0:
            q.append(0)
            c.append(cnt+1)
            q.append(1)
            c.append(cnt+1)


print(bfs())
"""
N=int(input())
def fib():
    a=1
    b=1
    for i in range(N-1):
        a,b= b,a+b
    return a
print(fib())

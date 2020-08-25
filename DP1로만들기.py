"""
from collections import deque
a=deque()
c=deque()
N=int(input())
def bfs(start):
    count=0
    a.append(start)
    c.append(count)
    while(a):
        start=a.popleft()
        count=c.popleft()
        if start==1:
            return count
        if start%3==0:
            a.append(start/3)
            c.append(count+1)
        if start%2==0:
            a.append(start/2)
            c.append(count+1)
        a.append(start-1)
        c.append(count+1)

print(bfs(N))
"""

"""

X = int(input())
count = 0
result = [X]
def calculation(x):
    lst = []
    for i in x:
        lst.append(i-1)
        if i%3 ==0:
            lst.append(i/3)
        if i%2 ==0:
            lst.append(i/2)
    lst = set(lst)
    lst = list(lst)
    return lst
while True:
    if X == 1:
        break
    temp = result
    result = []
    result = calculation(temp)
    count += 1
    if min(result) == 1:
        break
print(count)
"""

def min(x, y):
    return x if x <= y else y


x = int(input())

minimum_count = [0 for _ in range(x + 1)]

index = 0
while (True):
    if index > x:
        break

    if index <= 1:
        minimum_count[index] = 0
    else:
        temp_min = x + 1
        if index % 3 == 0:
            temp_index = int(index / 3)
            temp_min = min(temp_min, minimum_count[temp_index])

        if index % 2 == 0:
            temp_index = int(index / 2)
            temp_min = min(temp_min, minimum_count[temp_index])

        temp_min = min(temp_min, minimum_count[index - 1])
        minimum_count[index] = int(temp_min + 1)
        print(minimum_count)
    print(index)
    index = index + 1
print(minimum_count[x])





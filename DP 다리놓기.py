import itertools

case=int(input())
for i in range(case):
    n,m=input().split()
    lst=[0 for i in range(m)]
    answer=itertools.combiantions(lst,n)

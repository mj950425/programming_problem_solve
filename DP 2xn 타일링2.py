
N=int(input())
lst=[0 for i in range(N+1)]
lst[0]=1
lst[1]=3
for i in range(2,N):
    lst[i]=lst[i-2]*2+lst[i-1]
print(lst)
print(lst[N-1]%10007)
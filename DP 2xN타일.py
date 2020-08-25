N=int(input())

def fib(x):
    lst=[0 for i in range(x+1)]
    if x==1:
        return 1
    elif x==2:
        return 2
    else:
        lst[1]=1
        lst[2]=2
        for j in range(3,x+1):
            lst[j]=lst[j-1]+lst[j-2]
        return lst[x]%10007
print(fib(N))
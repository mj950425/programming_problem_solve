case=int(input())
answer=[]
for i in range(case):
    N=int(input())
    countone = [0 for i in range(N + 1)]
    countzero = [0 for i in range(N + 1)]

    if N==0:
        answer.append(1,0)
    elif N==1:
        print("0 1")
    elif N==2:
        print("1 1")
    elif N==3:
        print("1 2")
    else:

        countone[1]=1
        countone[2]=1
        countone[3]=2
        countzero[0]=1
        countzero[1]=0
        countzero[2]=1
        countzero[3]=1
        for j in range(N):
            if j >3:
                countone[j]=countone[j-1]+countone[j-2]
                countzero[j]=countzero[j-1]+countzero[j-2]

        print(countzero,countone)

    # 5를 호출
    # fib(4)+fib(3)
    # fib(3)+fib(2)+     fib(2)+fib(1)
    # fib(6)= fib(5)+fib(4)=fib(4)+fib(3)  +  fib(3)+fib(2)
    # = fib(3)+fib(2) + fib(3)   + fib(3)+fib(2)

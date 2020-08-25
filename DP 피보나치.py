
case = int(input())
for i in range(case):
    N=int(input())
    if N ==0:
        print(1,0)
    elif N==1:
        print(0,1)
    else:
        countone = [0 for i in range(N+1)]
        countzero = [0 for i in range(N+1)]

        countone[0]=0
        countone[1]=1

        countzero[0]=1
        countzero[1]=0

        for i in range(N+1):
            if i >1:
                countone[i]=countone[i-1]+countone[i-2]
                countzero[i]=countzero[i-1]+countzero[i-2]
                if i ==N:
                    print(countzero[i],countone[i])


N=int(input())
lst=[]
dp=[0 for i in range(N)]
for i in range(N):
    lst.append(int(input()))
def solution():
    if N ==1:
        print(lst[0])
    elif N ==2:
        print(lst[0]+lst[1])
    elif N ==3:
        print(max(lst[1]+lst[2],lst[0]+lst[2],lst[1]+lst[0]))
    else:
        dp[0]=lst[0]
        dp[1]=lst[1]+lst[0]
        dp[2]=max(lst[1]+lst[2],lst[0]+lst[2],lst[1]+lst[0])

        for i in range(3,N):
            dp[i]=max(dp[i-2]+lst[i],dp[i-3]+lst[i-1]+lst[i],dp[i-1])
        print(max(dp))
solution()
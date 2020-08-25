N=int(input())
step=[0]
answer=[0 for i in range(N+1)]
count=0
for i in range(N):
    step.append(int(input()))
def solution(N):
    for i in range(1,N+1):
        if N==1:
            return step[1]
        elif N==2:
            return step[2]+step[1]

        else:
            answer[1]=step[1]
            answer[2]=step[2]+step[1]
            answer[3]=max(step[1]+step[3],step[2]+step[3])
            answer[i]=step[i]+max(answer[i-2],answer[i-3]+step[i-1])
    return answer[N]
print(solution(N))

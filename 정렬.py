def solution(array, commands):
    ans=[]
    for i in range(len(commands)):
        answer = []
        answer=array[commands[i][0]-1:commands[i][1]]
        answer.sort()
        ans=ans+[answer[commands[i][2]-1]]
    return ans

"""
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
"""
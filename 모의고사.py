"""
https://programmers.co.kr/learn/courses/30/parts/12230
"""
answer = []
first=[]
second=[]
third=[]
while(len(first)<10000):
    first=first+[1,2,3,4,5]

while(len(second)<10000):
    second=second+[2,1,2,3,2,4,2,5]

while(len(third)<10000):
    third=third+[3,3,1,1,2,2,4,4,5,5]
def solution(answers):
    answer = []
    f = 0
    s = 0
    t = 0
    first = []
    second = []
    third = []
    while (len(first) < 10000):
        first = first + [1, 2, 3, 4, 5]

    while (len(second) < 10000):
        second = second + [2, 1, 2, 3, 2, 4, 2, 5]

    while (len(third) < 10000):
        third = third + [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if first[i] == answer[i]:
            f += 1
    for i in range(len(answers)):
        if second[i] == answer[i]:
            s += 1
    for i in range(len(answers)):
        if third[i] == answer[i]:
            t += 1


    if f > s and f > t:
        answer = [1]
    if s > f and s > t:
        answer = [2]
    if t > s and t > f:
        answer = [3]
    if t > s and t == f:
        answer = [1, 3]
    if s > t and s == f:
        answer = [1, 2]
    if t == s and s > f:
        answer = [2, 3]
    if t == s and s == f and t == f:
        answer = [1, 2, 3]

        return answer

"""
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
"""
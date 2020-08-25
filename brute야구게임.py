"""put = []
numbers = []
result = []
buf = 0
N = int(input())
for i in range(N):
    put.append(list(map(int, list(input().split()))))
for i in range(123, 1000):
    if "0" not in str(i):
        if len(set(str(i))) == 3:
            numbers.append(i)


def solution(answers):
    for k in numbers:
        buf = 0
        for i in range(N):
            strike = 0
            ball = 0
            for j in range(3):
                if ((str(answers[i][0]))[j] == (str(k))[j]):
                    strike = strike + 1
                if ((str(answers[i][0]))[j] != (
                        str(k))[j]) and ((str(answers[i][0]))[j] in str(k)):
                    ball = ball + 1
            if (answers[i][1] == strike) and (answers[i][2] == ball):
                buf = buf + 1

        if (buf == N):
            result.append(k)


solution(put)
print(len(result))"""
put = []
numbers = []
result = []
buf = 0
N = int(input())
for i in range(N):
    put.append(list(map(int, list(input().split()))))
for i in range(123, 1000):
    if "0" not in str(i):
        if len(set(str(i))) == 3:
            numbers.append(i)


def solution(answers):
    for k in numbers:
        buf = 0
        for i in range(N):
            strike = 0
            ball = 0
            for j in range(3):
                if ((str(answers[i][0]))[j] == (str(k))[j]):
                    strike = strike + 1
                if ((str(answers[i][0]))[j] != (
                        str(k))[j]) and ((str(answers[i][0]))[j] in str(k)):
                    ball = ball + 1
            if (answers[i][1] != strike) or (answers[i][2] != ball):
                break

        else:
            result.append(k)


solution(put)
print(len(result))
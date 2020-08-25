"""
https://programmers.co.kr/learn/courses/30/lessons/62049
"""

import sys

sys.setrecursionlimit(100000)

answer = []
count=0
def solution(n):
    global answer
    global count
    if count==n:
        return
    if not answer:
        answer.append(0)
    if answer:

        answer=answer+[0]+answer[::-1]
        count=count+1
        solution(n)
print(count)

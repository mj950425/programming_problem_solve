"""
https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3
"""
def solution(numbers):
    numbers=list(map(str(numbers)))
    numbers.sort(ket=lambda x:x*3,reverse=True)
    return numbers

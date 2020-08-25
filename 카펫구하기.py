"""
https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3
"""


def solution(brown, yellow):
    q = 0
    a = []
    for i in range(1, int((yellow + 1) / 2) + 1):
        if (yellow) % i == 0:

            q = (yellow) / i
            if 2 * q + 2 * i + 4 == brown:
                a = [2 + q, 2 + i]
                a.sort(reverse=True)
    return a

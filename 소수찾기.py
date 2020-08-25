"""
https://programmers.co.kr/learn/courses/30/parts/12230
"""
import itertools


def is_prime_not_bad(n):
    if n < 2:
        return False
    if n is 2:
        return True
    if n % 2 is 0:
        return False
    l = round(n ** 0.5) + 1
    for i in range(3, l, 2):
        if n % i is 0:
            return False
    return True


def solution(numbers):
    count = 0
    numbers = list(numbers)
    answer = 0
    for i in range(1, len(numbers) + 1):
        c = (list(map(''.join, itertools.permutations(numbers, i))))
        c = list(set(c))
        print(c)
        for _ in c:

            if _[0] != "0":
                if is_prime_not_bad(int(_)):
                    print(_)
                    count += 1

    return count

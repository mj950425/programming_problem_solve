"""
문자열 압축하기
https://programmers.co.kr/learn/courses/30/lessons/60057
"""
from collections import deque

def solution(s):

    answer = len(s)
    ss=len(s)
    count = 1
    for i in range(1, len(s) ):
        length = 0
        stack = deque()
        for k in range(len(s)//i):
            c=""
            for j in range(i):

                c = c + (s[j + i * k])
            if stack:
                buf = stack[-1]
                if buf == c:
                    count = count + 1
                    if k==(len(s)//i) -1:
                        stack[-1] = stack[-1] + str(count)

                if buf != c and count == 1:
                    stack.append(c)
                if buf != c and count != 1:
                    stack[-1] = stack[-1] + str(count)
                    stack.append(c)
                    count = 1
            else:
                stack.append(c)
        for m in stack:
            length += len(m)

        length = length + (len(s) % i)

        if answer > length:
            answer = length
    print(answer)
    return answer

"""
#다른 사람의 파이썬스러운 코드
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))
"""

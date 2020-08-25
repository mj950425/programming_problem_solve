"""
https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
"""
from collections import deque

st = deque()


def solution(board, moves):
    answer = 0
    N = len(board)
    for i in range(len(moves)):
        moves[i] = moves[i] - 1
    for i in moves:
        for j in range(N):
            if board[j][i] != 0:


                buf = board[j][i]
                board[j][i] = 0
                if st:
                    bu = st.pop()
                    if buf == bu:
                        answer += 1
                    if bu != buf:
                        st.append(bu)
                        st.append(buf)
                else:
                    st.append(buf)

                break
    answer = answer * 2
    return answer
N, M, x, y, k = list(map(int, input().split()))
A=[]
graph=[]
#  0:맨위 1:아래 2:오른쪽 3:왼쪽 4:앞 5:뒤
dice = [0, 0, 0, 0, 0, 0]
for i in range(N):
    A =list(map(int, input().split()))
    graph.append(A)
command = list(map(int, input().split()))


# 1:동쪽 2:서쪽 3:북쪽 4:남쪽
def check(y, x):
    if y > N - 1 or y < 0 or x > M - 1 or x < 0:
        return False
    return True


buf = 0
for i in command:
    if i == 1:
        if check(y, x + 1):
            x = x + 1
            y = y
            buf = dice[3]
            dice[3] = dice[1]
            dice[1] = dice[2]
            dice[2] = dice[0]
            dice[0] = buf
            if graph[y][x] == 0:
                graph[y][x] = dice[1]
            dice[1] = graph[y][x]
            graph[y][x] = 0
            print(dice[0])

    elif i == 2:
        if check(y, x - 1):
            x = x - 1
            y = y
            buf = dice[0]
            dice[0] = dice[2]
            dice[2] = dice[1]
            dice[1] = dice[3]
            dice[3] = buf
            if graph[y][x] == 0:
                graph[y][x] = dice[1]
            dice[1] = graph[y][x]
            graph[y][x] = 0
            print(dice[0])

    elif i == 3:
        if check(y - 1, x):
            y = y - 1
            x = x
            buf = dice[5]
            dice[5] = dice[0]
            dice[0] = dice[4]
            dice[4] = dice[1]
            dice[1] = buf
            if graph[y][x] == 0:
                graph[y][x] = dice[1]
            dice[1] = graph[y][x]
            graph[y][x] = 0
            print(dice[0])

    elif i == 4:
        if check(y + 1, x):
            y = y + 1
            x = x
            buf = dice[0]
            dice[0] = dice[5]
            dice[5] = dice[1]
            dice[1] = dice[4]
            dice[4] = buf
            if graph[y][x] == 0:
                graph[y][x] = dice[1]
            dice[1] = graph[y][x]
            graph[y][x] = 0
            print(dice[0])






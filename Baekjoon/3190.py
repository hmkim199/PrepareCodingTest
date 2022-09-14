# https://www.acmicpc.net/problem/3190
# 뱀

from collections import deque


N = int(input())
K = int(input())
move = [(1, 0), (0, -1), (-1, 0), (0, 1)] # 아 왼 위 오
dir = 3 # 현재 방향은 오른쪽

board = [[False for _ in range(N+1)] for _ in range(N+1)]

for _ in range(K):
    row, col = map(int, input().split())
    board[row][col] = True

L = int(input())
change = deque()
for _ in range(L):
    X, C = input().split()
    change.append([X, C])

time = 0
snake = deque([[1, 1]])
while True:
    if change and time == int(change[0][0]):
        x, c = change.popleft()
        if c == "D": # 오른쪽
            dir = (dir+1)%4
        else:
            dir = (dir-1)%4

    time += 1
    head = snake[0]
    x = head[0] # row
    y = head[1] # col
    dx = move[dir][0]
    dy = move[dir][1]
    if 0 < x+dx <= N and 0 < y+dy <= N:
        if [x+dx, y+dy] in snake:
            break
        snake.appendleft([x+dx, y+dy])
        if not board[x+dx][y+dy]: # 없으면
            snake.pop()
        else:
            board[x+dx][y+dy] = False
    else:
        break

print(time)



# https://www.acmicpc.net/problem/12100
# 2048 (Easy)

from collections import deque
from copy import deepcopy


N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def move_x(start, end, step, j, board):
    value = []
    check = 0
    for i in range(start, end, step):
        if board[i][j] == 0:
            continue
        if board[i][j] == check:
            value.append(check * 2)
            check = 0
        elif check == 0:
            check = board[i][j]
        else:
            value.append(check)
            check = board[i][j]
        board[i][j] = 0
    
    if check != 0:
        value.append(check)
    
    return value

def move_y(start, end, step, i, board):
    value = []
    check = 0
    for j in range(start, end, step):
        if board[i][j] == 0:
            continue
        if board[i][j] == check:
            value.append(check * 2)
            check = 0
        elif check == 0:
            check = board[i][j]
        else:
            value.append(check)
            check = board[i][j]
        board[i][j] = 0
    
    if check != 0:
        value.append(check)
    
    return value

def move_up(board, N):
    # 위로 합치기
    for j in range(N):
        value = move_x(0, N, 1, j, board)

        for i in range(len(value)):
            board[i][j] = value[i]

    return board

def move_down(board, N):
    # 아래로 합치기
    for j in range(N):
        value = move_x(N-1, -1, -1, j, board)
        
        for i in range(N-1, N - len(value)-1, -1):
            board[i][j] = value[N-i-1]

    return board

def move_left(board, N):
    # 왼쪽으로 합치기
    for i in range(N):
        value = move_y(0, N, 1, i, board)
        
        for j in range(len(value)):
            board[i][j] = value[j]
    
    return board

def move_right(board, N):
    # 오른쪽으로 합치기
    for i in range(N):
        value = move_y(N-1, -1, -1, i, board)
        
        for j in range(N-1, N - len(value)-1, -1):
            board[i][j] = value[N-j-1]
    
    return board

def game2048(board):
    result = 0
    q = deque()
    q.append((board, 0)) # 0은 움직인 횟수
    while q:
        b, count = q.popleft()

        if count >= 5:
            result = max(result, max(map(max, b)))
            continue

        q.append((move_up(deepcopy(b), N), count+1))
        q.append((move_down(deepcopy(b), N), count+1))
        q.append((move_left(deepcopy(b), N), count+1))
        q.append((move_right(deepcopy(b), N), count+1))

    return result

print(game2048(board))
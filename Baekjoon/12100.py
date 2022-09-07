# https://www.acmicpc.net/problem/12100
# 2048 (Easy)

from collections import deque
from copy import deepcopy


N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def move_up(board, N):
    # 위로 합치기
    for j in range(N):
        value = []
        cur = 0
        for i in range(N):
            if board[i][j] == 0:
                cur = 0
                continue

            if board[i][j] == cur:
                value.append(cur * 2)
                board[i][j] = 0
                cur = 0
            elif cur == 0:
                cur = board[i][j]
            else:
                value.append(cur)
                cur = board[i][j]
        if cur != 0:
            value.append(cur)

        for i in range(len(value)):
            board[i][j] = value[i]

    return board

# def move_up(board, N):
#     # 위로 합치기
#     for j in range(N):
#         value = []
#         for i in range(N):
#             if board[i][j] == 0:
#                 continue
#             if i!= N-1 and board[i][j] == board[i+1][j]:
#                 value.append(board[i][j]*2)
#                 board[i][j] = 0
#                 board[i+1][j] = 0
#             else:
#                 value.append(board[i][j])
#                 board[i][j] = 0
        
#         for i in range(len(value)):
#             board[i][j] = value[i]

#     return board

def move_down(board, N):
    # 아래로 합치기
    for j in range(N):
        value = []
        for i in range(N-1, -1, -1):
            if board[i][j] == 0:
                continue
            if i!= 0 and board[i][j] == board[i-1][j]:
                value.append(board[i][j]*2)
                board[i][j] = 0
                board[i-1][j] = 0
            else:
                value.append(board[i][j])
                board[i][j] = 0
        
        for i in range(N-1, N - len(value)-1, -1):
            board[i][j] = value[N-i-1]

    return board

def move_left(board, N):
    # 왼쪽으로 합치기
    for i in range(N):
        value = []
        for j in range(N):
            if board[i][j] == 0:
                continue
            if j!= N-1 and board[i][j] == board[i][j+1]:
                value.append(board[i][j]*2)
                board[i][j] = 0
                board[i][j+1] = 0
            else:
                value.append(board[i][j])
                board[i][j] = 0
        
        for j in range(len(value)):
            board[i][j] = value[j]
    
    return board

def move_right(board, N):
    # 오른쪽으로 합치기
    for i in range(N):
        value = []
        for j in range(N-1, -1, -1):
            if board[i][j] == 0:
                continue
            if j!= 0 and board[i][j] == board[i][j-1]:
                value.append(board[i][j]*2)
                board[i][j] = 0
                board[i][j-1] = 0
            else:
                value.append(board[i][j])
                board[i][j] = 0
        
        # print(*value)
        for j in range(N-1, N - len(value)-1, -1):
            # print(j, len(value)-1-j)
            board[i][j] = value[N-j-1]
    
    return board

def game2048(board):
    result = 0
    q = deque()
    q.append((board, 0)) # 0은 움직인 횟수
    while q:
        b, count = q.popleft()
        if count == 4:
            print(*b, sep="\n")
            print("=======================\n")
        if count >= 5:
            result = max(result, max(map(max, b)))
            continue
        
        # print(*b, sep="\n")
        # print("origin\n")
        up = move_up(deepcopy(b), N)
        down = move_down(deepcopy(b), N)
        left = move_left(deepcopy(b), N)
        right = move_right(deepcopy(b), N)
        # print(*up, sep="\n")
        # print("up\n")
        # print(*down, sep="\n")
        # print("down\n")
        # print(*left, sep="\n")
        # print("left\n")
        # print(*right, sep="\n")
        # print("right\n")
        q.append((up, count+1))
        q.append((down, count+1))
        q.append((left, count+1))
        q.append((right, count+1))
        # break

    return result

print(game2048(board))
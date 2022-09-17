# https://www.acmicpc.net/problem/14502
# 연구소

from collections import deque
from copy import deepcopy
from itertools import combinations

N, M = map(int, input().split())
pos = [(i, j) for j in range(M) for i in range(N)]

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

walls = list(combinations(pos, 3))

safe = 0
for wall in walls:
    if board[wall[0][0]][wall[0][1]] != 0:
        continue
    elif board[wall[1][0]][wall[1][1]] != 0:
        continue
    elif board[wall[2][0]][wall[2][1]] != 0:
        continue
    
    new_board = deepcopy(board)
    new_board[wall[0][0]][wall[0][1]] = 1
    new_board[wall[1][0]][wall[1][1]] = 1
    new_board[wall[2][0]][wall[2][1]] = 1

    q = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if new_board[i][j] == 2 and not visited[i][j]:
                visited[i][j] = True
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        if 0 <= x+dx < N and 0 <= y+dy < M and not visited[x+dx][y+dy]:
                            if new_board[x+dx][y+dy] == 0:
                                visited[x+dx][y+dy] = True
                                new_board[x+dx][y+dy] = 2
                                q.append((x+dx, y+dy))
    
    count = 0
    for i in range(N):
        for j in range(M):
            if new_board[i][j] == 0:
                count += 1
    safe = max(safe, count)

print(safe)
# https://www.acmicpc.net/problem/12100
# 2048 (Easy)

from collections import deque


N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def game2048(board):
    q = deque()
    q.append([board, 0]) # board, count
    while q:
        board, count = q.popleft()
        if count >= 5:
            continue
        for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            return
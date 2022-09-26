# https://www.acmicpc.net/problem/14503
# 로봇 청소기

N, M = map(int, input().split())
r, c, d = map(int, input().split()) # d: 0 1 2 3 -> 북 동 남 서
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북 동 남 서 (dx, dy)
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

cleaned = [[False for _ in range(M)] for _ in range(N)]

while True:
    if not cleaned[r][c]:
        cleaned[r][c] = True

    for _ in range(4):
        d = (d - 1) % len(dir) # 왼쪽 회전
        new_r = r + dir[d][0] # 회전한 방향으로 이동
        new_c = c + dir[d][1]
        if 0 <= new_r < N and 0 <= new_c < M and board[new_r][new_c] != 1 and not cleaned[new_r][new_c]:
            cleaned[new_r][new_c] = True
            r = new_r
            c = new_c
            break
    else:
        r -= dir[d][0] # 기존 방향으로 후진
        c -= dir[d][1]
        if board[r][c] == 1:
            break

count = 0
for i in range(N):
    for j in range(M):
        if cleaned[i][j]:
            count += 1

print(count)
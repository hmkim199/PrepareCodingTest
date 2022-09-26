# https://www.acmicpc.net/problem/14503
# 로봇 청소기

N, M = map(int, input().split())
r, c, d = map(int, input().split()) # d: 0 1 2 3 -> 북 동 남 서
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북 동 남 서 (dx, dy)
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

visited = [[False for _ in range(M)] for _ in range(N)]

while True:
    if not visited[r][c]:
        visited[r][c] = True

    for _ in range(4):
        d = (d - 1) % len(dir)
        new_x = r + dir[d][0]
        new_y = c + dir[d][1]
        if 0 <= new_x < N and 0 <= new_y < M and board[new_x][new_y] != 1 and not visited[new_x][new_y]:
            visited[new_x][new_y] = True
            r = new_x
            c = new_y
            break
    else:
        r -= dir[d][0]
        c -= dir[d][1]
        if board[r][c] == 1:
            break

clean = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            clean += 1

print(clean)
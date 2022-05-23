# https://www.acmicpc.net/problem/10026
# 적록색약

from collections import deque

N = int(input())
pic = []
for _ in range(N):
    pic.append(list(input()))

def bfs(queue, visited):
    while queue:
        x, y = queue.popleft()
        for dx, dy in ([0, 1], [1, 0], [0, -1], [-1, 0]):
            if x+dx < 0 or x+dx >= N or y+dy < 0 or y+dy >= N:
                continue

            if pic[x+dx][y+dy] == pic[x][y] and not visited[x+dx][y+dy]:
                visited[x+dx][y+dy] = True
                queue.append([x+dx, y+dy])
    return visited

def count():
    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                cnt += 1
                visited[i][j] = True
                visited = bfs(deque([[i, j]]), visited)
    return cnt

def change_RtoG(pic, N):
    for i in range(N):
        for j in range(N):
            if pic[i][j] == "R":
                pic[i][j] = "G"
    return pic

cnt = count()
pic = change_RtoG(pic, N)
b_cnt = count()

print(cnt, b_cnt)

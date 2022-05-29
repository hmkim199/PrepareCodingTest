# https://www.acmicpc.net/problem/11403
# 경로 찾기

from collections import deque


N = int(input())
adjacent_matrix = []
visited = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(N):
    adjacent_matrix.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            queue = deque()
            queue.append([i, j])
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if x+dx < 0 or x+dx >= N or y+dy < 0 or y+dy >= N:
                        continue
                    if not visited[x+dx][y+dy] and (adjacent_matrix[x+dx][y+dy] == 1 or x+dx==y+dy):
                        visited[x+dx][y+dy] = 1
                        queue.append([x+dx, y+dy])

print(*visited, sep="\n")
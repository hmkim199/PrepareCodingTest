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
        if not visited[i][j] and adjacent_matrix[i][j] == 1:
            queue = deque()
            queue.append([i, j])
            while queue:
                x, y = queue.popleft()
                for k in range(N):
                    if adjacent_matrix[y][k] == 1 and not visited[y][k]:
                        visited[y][k] = 1
                        visited[x][k] = 1
                        visited[i][k] = 1
                        queue.append([y, k])
        if i==j:
            visited[i][j] = 1

print(*visited, sep="\n")
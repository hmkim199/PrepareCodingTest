# https://www.acmicpc.net/problem/1504
# 특정한 최단 경로

from collections import deque


N, E = map(int, input().split())
matrix = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(E):
    a, b, c = map(int, input().split())
    matrix[a][b] = c
    matrix[b][a] = c

v1, v2 = map(int, input().split())

def bfs(a, b):
    q = deque()
    for i in range(a, N):
        for j in range(N):
            if matrix[i][j] > 0:
                q.append([i, j, matrix[i][j]])

                while 
# 1 - v1 - v2 - n 의 최소 거리: bfs(1, v1) + bfs(v1, v2) + bfs(v2, n)
# 1 - v2 - v1 - n 의 최소 거리: bfs(1, v2) + bfs(v2, v1) + bfs(v1, n)


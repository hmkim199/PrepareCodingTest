# DFS와 BFS
# https://www.acmicpc.net/problem/1260

from collections import deque


n, m, v = map(int, input().split())
matrix = [[0 for i in range(n+1)] for j in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

def dfs(v, visited):
    visited.append(v)
    for i in range(len(matrix[v])):
        if matrix[v][i] == 1 and i not in visited:
            dfs(i, visited)
    return visited

def bfs(v):
    queue = deque()
    queue.append(v)
    visited = [v]
    while queue:
        now = queue.popleft()
        for i in range(len(matrix[now])):
            if matrix[now][i] == 1 and i not in visited:
                queue.append(i)
                visited.append(i)
    return visited


print(*dfs(v, []))
print(*bfs(v))
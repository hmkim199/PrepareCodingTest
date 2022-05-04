# DFS와 BFS 
# https://www.acmicpc.net/problem/1260

from collections import deque


N, M, V = map(int, input().split())
adjacent_list = [
    [] for _ in range(N+1)
]
visited = [False for _ in range(N+1)]
dfs_result = []
bfs_result = []

for _ in range(M):
    a, b = map(int, input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)

for i in range(1, N+1):
    adjacent_list[i] = sorted(adjacent_list[i])

def dfs(v):
    global visited
    
    if not visited[v]:
        visited[v] = True
        dfs_result.append(v)
        for neighbor in adjacent_list[v]:
            dfs(neighbor)

def bfs(v):
    visited = [False for _ in range(N+1)]

    queue = deque([v])
    visited[v] = True
    bfs_result.append(v)
    while queue:
        now = queue.popleft()
        for neighbor in adjacent_list[now]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                bfs_result.append(neighbor)

dfs(V)
bfs(V)

print(*dfs_result)
print(*bfs_result)
        
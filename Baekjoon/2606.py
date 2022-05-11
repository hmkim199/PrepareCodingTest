# https://www.acmicpc.net/problem/2606
# 바이러스 

# 풀이 1. 풀이 2보다 시간, 공간 효율 높음
n = int(input())
m = int(input())
v = 1
matrix = [[0 for i in range(n+1)] for j in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

def bfs(v):
    queue = [v]
    visited = [v]
    while len(queue) > 0:
        now = queue.pop(0)
        for i in range(len(matrix[now])):
            if matrix[now][i] == 1 and i not in visited:
                queue.append(i)
                visited.append(i)
    return len(visited)-1

print(bfs(v))

# 풀이 2
from collections import deque

N = int(input())
edge = int(input())
connected = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(edge):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)

def bfs(v, connected):
    queue = deque()
    queue.append(v)
    visited[v] = True

    count = 0
    while queue:
        now = queue.popleft()
        for neighbor in connected[now]:
            if not visited[neighbor]:
                visited[neighbor] = True
                count += 1
                queue.append(neighbor)

    return count

print(bfs(1, connected))
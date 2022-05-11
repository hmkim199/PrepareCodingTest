# https://www.acmicpc.net/problem/2606
# 바이러스 

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
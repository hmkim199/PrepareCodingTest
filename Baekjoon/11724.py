# https://www.acmicpc.net/problem/11724
# 연결 요소의 개수

# pypy로 통과

from collections import deque


N, M = map(int, input().split())

V = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    V[x][y] = 1
    V[y][x] = 1


count = 0
visited = [False] * N
for i in range(N):
    for j in range(N): 
        if V[i][j] == 1 and not visited[j]:
            visited[j] = True
            count += 1
            queue = deque()
            queue.append(j)
            while queue:
                now = queue.popleft()
                for k in range(N):
                    if V[now][k] == 1 and not visited[k]:
                        visited[k] = True
                        queue.append(k)

# 방문 안한 노드는 혼자 있는 노드!! 얘네도 count에 포함시켜줘야 함.
for i in range(N):
    if not visited[i]:
        count += 1
print(count)

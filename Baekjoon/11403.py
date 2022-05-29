# https://www.acmicpc.net/problem/11403
# 경로 찾기

from collections import deque
from copy import deepcopy


N = int(input())
adj = []

for _ in range(N):
    adj.append(list(map(int, input().split())))

answer = deepcopy(adj)

for i in range(N):
    for j in range(N):
        if adj[i][j] == 1:
            visited = [False] * N
            queue = deque()
            visited[j] = True
            queue.append(j)
            while queue:
                now = queue.popleft()
                for k in range(N):
                    if adj[now][k] == 1 and now != i and not visited[k]:
                        answer[i][k] = 1
                        visited[k] = True
                        queue.append(k)

for i in range(N):
    print(*answer[i])
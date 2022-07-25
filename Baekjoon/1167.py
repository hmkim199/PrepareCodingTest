# https://www.acmicpc.net/problem/1167
# 트리의 지름

from collections import deque


V = int(input())
adjacent = [[-1 for _ in range(V)] for _ in range(V)]
visited = [False for _ in range(V)]


for _ in range(V):
    info = list(map(int, input().split()))
    adjacent[info[0]-1][info[0]-1] = 0

    v = 0
    dist = 0
    for i in range(1, len(info)-1):
        if i%2 == 1:
            v = info[i]
        elif i != -1:
            dist = info[i]
            adjacent[info[0]-1][v-1] = dist

# print(adjacent)
max_dist = 0
q = deque()
for i in range(V):
    visited[i] = True
    for j in range(V):
        if not visited[j] and adjacent[i][j] > 0:
            visited[j] = True
            q.append([j, adjacent[i][j]])
            max_dist = max(max_dist, adjacent[i][j])
            while q:
                prev, dist = q.popleft()
                max_dist = max(max_dist, dist)
                for k in range(V):
                    if not visited[k] and adjacent[prev][k] > 0:
                        visited[k] = True
                        q.append([k, dist + adjacent[prev][k]])

print(max_dist)
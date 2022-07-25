# https://www.acmicpc.net/problem/1167
# 트리의 지름

from collections import deque


V = int(input())
adjacent = [dict() for _ in range(V)]
visited = [False for _ in range(V)]


for _ in range(V):
    info = list(map(int, input().split()))
    # adjacent[info[0]-1][info[0]-1] = 0

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
        adj_dist = adjacent[i].get(j)
        if not visited[j] and adj_dist:
            visited[j] = True
            q.append([j, adj_dist])
            max_dist = max(max_dist, adj_dist)
            while q:
                prev, dist = q.popleft()
                max_dist = max(max_dist, dist)
                for k in range(V):
                    new_adj_dist = adjacent[prev].get(k)
                    if not visited[k] and new_adj_dist:
                        visited[k] = True
                        q.append([k, dist + new_adj_dist])

print(max_dist)
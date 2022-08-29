# https://www.acmicpc.net/problem/1967
# 트리의 지름

import heapq

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    parent, child, cost = map(int, input().split())
    tree[parent].append([child, cost])
    tree[child].append([parent, cost])

def dijkstra(start):
    dist = [10e9 for _ in range(n+1)]
    dist[start] = dist[0] = 0
    q = []
    heapq.heappush(q, (dist[start], start))

    while q:
        now_dist, node = heapq.heappop(q)

        if dist[node] < now_dist:
            continue

        for adj_node, adj_dist in tree[node]:
            if dist[adj_node] > dist[node] + adj_dist:
                dist[adj_node] = dist[node] + adj_dist
                heapq.heappush(q, (dist[adj_node], adj_node))
    
    max_dist = max(dist)
    node = dist[1:].index(max_dist) + 1 # 노드 0 제외
    return node, max_dist

idx, max_dist = dijkstra(1)
idx, max_dist = dijkstra(idx)
print(max_dist)
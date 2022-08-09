# https://www.acmicpc.net/problem/1238
# 파티 

import heapq
import sys


input = sys.stdin.readline
N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    # print(a, b, t)
    graph[a].append((b, t))

# print(graph)

def dijkstra(start, end):
    # start 노드로부터 각각 노드까지의 최단 거리 구해주는 다익스트라 함수.
    dist = [10e9 for _ in range(N+1)]
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        now_dist, node = heapq.heappop(q)
        if dist[node] < now_dist:
            continue

        # 인접한 노드 중 complete하지 않은 노드 relax
        for adj in graph[node]:
            adj_node = adj[0]
            adj_dist = adj[1]
            if dist[node] + adj_dist < dist[adj_node]:
                dist[adj_node] = dist[node] + adj_dist
                heapq.heappush(q, (dist[adj_node], adj_node))
    
    return dist[end]

maximum = 0
for i in range(1, N+1):
    maximum = max(maximum, dijkstra(i, X) + dijkstra(X, i))

print(maximum)
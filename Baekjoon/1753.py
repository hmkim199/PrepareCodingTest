# https://www.acmicpc.net/problem/1753
# 최단경로

import heapq
import sys


input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    dist = [10e9 for _ in range(V+1)]
    dist[start] = 0
    q = []
    heapq.heappush(q, (dist[start], start))
    while q:
        cur_dist, cur_node = heapq.heappop(q)
        if dist[cur_node] < cur_dist:
            continue

        for adj_node, adj_dist in graph[cur_node]:
            if dist[adj_node] > dist[cur_node] + adj_dist:
                dist[adj_node] = dist[cur_node] + adj_dist
                heapq.heappush(q, (dist[adj_node], adj_node))

    return dist[1:]

result = dijkstra(K) # 이걸 1로 해서 틀렸었다 ㅋㅋㅋㅋㅋㅋㅋㅋ 
for res in result:
    if res >= 10e9:
        print("INF")
    else:
        print(res)
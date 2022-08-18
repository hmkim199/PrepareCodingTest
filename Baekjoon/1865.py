# https://www.acmicpc.net/problem/1865
# 웜홀

import heapq
import sys


input = sys.stdin.readline

TC = int(input())

def dijkstra(N, graph, start):
    dist = [10e9 for _ in range(N+1)]
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
                if adj_node == start and dist[start] < 0:
                    return dist[start]
                heapq.heappush(q, (dist[adj_node], adj_node))
        
    return dist[start]


for _ in range(TC):
    N, M, W = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        S, E, T = map(int, input().split())
        graph[S].append((E, T))
        graph[E].append((S, T))
    
    for _ in range(W):
        S, E, T = map(int, input().split())
        T = -T if T > 0 else T
        graph[S].append((E, T))
        # graph[E].append((S, T))
    
    res = dijkstra(N, graph, 1)
    if res >= 0:
        print("NO")
    else:
        print("YES")

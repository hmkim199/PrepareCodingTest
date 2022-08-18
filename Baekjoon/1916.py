# https://www.acmicpc.net/problem/1865
# 웜홀

import heapq
import sys


input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, dest, price = map(int, input().split())
    graph[start].append((dest, price))

start, dest = map(int, input().split())

def dijkstra(start, dest):
    dist = [10e9 for _ in range(N+1)]
    dist[start] = 0
    q = []
    heapq.heappush(q, (dist[start], start))

    while q:
        cur_dist, cur_node = heapq.heappop(q)

        if dist[cur_node] < cur_dist: # =을 넣으면 틀림.
            continue

        for adj_node, adj_dist in graph[cur_node]:
            if dist[adj_node] > dist[cur_node] + adj_dist:
                dist[adj_node] = dist[cur_node] + adj_dist
                heapq.heappush(q, (dist[adj_node], adj_node))
    
    return dist[dest]

print(dijkstra(start, dest))

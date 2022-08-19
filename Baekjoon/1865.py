# https://www.acmicpc.net/problem/1865
# 웜홀

# 다익스트라로 풀려고 했으나 틀렸습니다 -> 음의 간선이 있을 때 다익스트라는 못 쓴다는 사실을 까먹음.

# import heapq
# import sys


# input = sys.stdin.readline

# TC = int(input())

# def dijkstra(N, graph, start):
#     dist = [10e9 for _ in range(N+1)]
#     dist[start] = 0
#     q = []
#     heapq.heappush(q, (dist[start], start))

#     while q:
#         cur_dist, cur_node = heapq.heappop(q)

#         if dist[cur_node] < cur_dist:
#             continue

#         for adj_node, adj_dist in graph[cur_node]:
#             if dist[adj_node] > dist[cur_node] + adj_dist:
#                 dist[adj_node] = dist[cur_node] + adj_dist
#                 if adj_node == start and dist[start] < 0:
#                     return dist[start]
#                 heapq.heappush(q, (dist[adj_node], adj_node))
        
#     return dist[start]


# for _ in range(TC):
#     N, M, W = map(int, input().split())
#     graph = [[] for _ in range(N+1)]

#     for _ in range(M):
#         S, E, T = map(int, input().split())
#         graph[S].append((E, T))
#         graph[E].append((S, T))
    
#     for _ in range(W):
#         S, E, T = map(int, input().split())
#         T = -T if T > 0 else T
#         graph[S].append((E, T))
#         # graph[E].append((S, T))
    
#     res = dijkstra(N, graph, 1)
#     if res >= 0:
#         print("NO")
#     else:
#         print("YES")


# 음의 순환이 있을 때 최단 경로를 다익스트라로 찾을 수 없다! 따라서 벨만 포드 알고리즘 사용한다.
# 벨만포드 가장 잘 설명된 유튜브 링크 : https://www.youtube.com/watch?v=0NrlN88D9Fs

# 틀렸습니다.
import sys

input = sys.stdin.readline

TC = int(input())

def bellman_ford(N, edges, start):
    dist = [10e9 for _ in range(N+1)]
    dist[start] = 0

    for i in range(N-1):
        for s, e, t in edges:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                
    return dist[start]

for _ in range(TC):
    N, M, W = map(int, input().split())
    # graph = [[] for _ in range(N+1)]
    edges = []

    for _ in range(M):
        S, E, T = map(int, input().split())
        # graph[S].append((E, T))
        # graph[E].append((S, T))
        edges.append((S, E, T))
        edges.append((E, S, T))
    
    for _ in range(W):
        S, E, T = map(int, input().split())
        T = -T if T > 0 else T
        # graph[S].append((E, T))
        edges.append((S, E, T))
    
    res = bellman_ford(N, edges, 1)
    if res >= 0:
        print("NO")
    else:
        print("YES")


# https://www.acmicpc.net/problem/1504
# 특정한 최단 경로

# 정점의 개수 N과 간선의 개수 E
# 1 - v1 - v2 - n 의 최소 거리: 최소(1, v1) + 최소(v1, v2) + 최소(v2, n)
# 1 - v2 - v1 - n 의 최소 거리: 최소(1, v2) + 최소(v2, v1) + 최소(v1, n)

import sys
import heapq

input = sys.stdin.readline # 이거 없이 그냥 input함수로 하면 시간초과...
N, E = map(int, input().split())
adjacent = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adjacent[a].append((b, c))
    adjacent[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
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
        for adj in adjacent[node]:
            adj_node = adj[0]
            adj_dist = adj[1]
            if dist[node] + adj_dist < dist[adj_node]:
                dist[adj_node] = dist[node] + adj_dist
                heapq.heappush(q, (dist[adj_node], adj_node))
    
    return dist

start_1 = dijkstra(1)
start_v1 = dijkstra(v1)
start_v2 = dijkstra(v2)

distance = min(start_1[v1] + start_v1[v2] + start_v2[N], start_1[v2] + start_v2[v1] + start_v1[N])
if distance >= 10e9: # 여기 = 안 넣으면 틀림..
    print(-1)
else:
    print(distance)

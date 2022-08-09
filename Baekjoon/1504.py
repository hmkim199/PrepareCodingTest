# https://www.acmicpc.net/problem/1504
# 특정한 최단 경로

# from collections import deque


# N, E = map(int, input().split())
# matrix = [[0 for _ in range(N)] for _ in range(N)]
# for _ in range(E):
#     a, b, c = map(int, input().split())
#     matrix[a][b] = c
#     matrix[b][a] = c

# v1, v2 = map(int, input().split())

# def bfs(a, b):
#     q = deque()
#     for i in range(a, N):
#         for j in range(N):
#             if matrix[i][j] > 0:
#                 q.append([i, j, matrix[i][j]])

#                 while 



# 시간 초과

# 정점의 개수 N과 간선의 개수 E
# 1 - v1 - v2 - n 의 최소 거리: 최소(1, v1) + 최소(v1, v2) + 최소(v2, n)
# 1 - v2 - v1 - n 의 최소 거리: 최소(1, v2) + 최소(v2, v1) + 최소(v1, n)

from collections import deque


N, E = map(int, input().split())
adjacent = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adjacent[a].append((b, c))
    adjacent[b].append((a, c))

v1, v2 = map(int, input().split())

# print(adjacent)

def find_node_to_relax(complete, dist):
    node = 0
    for i in range(len(dist)):
        if not complete[i] and dist[i] < dist[node]:
            node = i
    return node

def dijkstra(start, end):
    # start 노드로부터 각각 노드까지의 최단 거리 구해주는 다익스트라 함수.
    dist = [10e9 for _ in range(N+1)]
    dist[start] = 0
    complete = [0 for _ in range(N+1)] # 최단 거리를 찾았는지 저장

    while sum(complete) < len(dist):
        # 아직 complete 되지 않은 노드 중 가장 거리 작은 노드 구하기
        node = find_node_to_relax(complete, dist)

        # 인접한 노드 중 complete하지 않은 노드 relax
        for adj in adjacent[node]:
            adj_node = adj[0]
            adj_dist = adj[1]
            if not complete[adj_node]:
                dist[adj_node] = min(dist[adj_node], dist[node] + adj_dist)
        
        # 현재 노드 complete 처리
        complete[node] = 1
    
    return dist[end]
    
    
distance = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N), dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N))
if distance > 10e9:
    print(-1)
else:
    print(distance)

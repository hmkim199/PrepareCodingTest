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



# 정점의 개수 N과 간선의 개수 E
# 1 - v1 - v2 - n 의 최소 거리: 최소(1, v1) + 최소(v1, v2) + 최소(v2, n)
# 1 - v2 - v1 - n 의 최소 거리: 최소(1, v2) + 최소(v2, v1) + 최소(v1, n)

from collections import deque


N, E = map(int, input().split())
adjacent = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adjacent[a] = (b, c)
    adjacent[b] = (a, c)

v1, v2 = map(int, input().split())

def dijkstra(start):
    # start 노드로부터 각각 노드까지의 최단 거리 구해주는 다익스트라 함수.
    dist = [10e9 for _ in range(N+1)]
    dist[start] = 0
    complete = [False for _ in range(N+1)] # 최단 거리를 찾았는지 저장
    complete[start] = True

    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        if adjacent[node]:
            next = sorted(adjacent[node], key=lambda x: x[1])[0]
            
    


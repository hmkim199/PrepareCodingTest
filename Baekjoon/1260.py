# # DFS와 BFS 
# # https://www.acmicpc.net/problem/1260

# from collections import deque


# N, M, V = map(int, input().split())
# adjacent_list = [
#     [] for _ in range(N+1)
# ]
# visited = [False for _ in range(N+1)]
# dfs_result = []
# bfs_result = []

# for _ in range(M):
#     a, b = map(int, input().split())
#     adjacent_list[a].append(b)
#     adjacent_list[b].append(a)

# for i in range(1, N+1):
#     adjacent_list[i] = sorted(adjacent_list[i])

# def dfs(v):
#     global visited
    
#     if not visited[v]:
#         visited[v] = True
#         dfs_result.append(v)
#         for neighbor in adjacent_list[v]:
#             dfs(neighbor)

# def bfs(v):
#     visited = [False for _ in range(N+1)]

#     queue = deque([v])
#     visited[v] = True
#     bfs_result.append(v)
#     while queue:
#         now = queue.popleft()
#         for neighbor in adjacent_list[now]:
#             if not visited[neighbor]:
#                 queue.append(neighbor)
#                 visited[neighbor] = True
#                 bfs_result.append(neighbor)

# dfs(V)
# bfs(V)

# print(*dfs_result)
# print(*bfs_result)
        
from collections import deque


N, M, V = map(int, input().split()) # 정점의 개수, 간선의 개수, 탐색 시작 정점 번호

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split()) # 간선이 연결하는 두 정점
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    if graph[i]:
        graph[i] = sorted(graph[i]) # 방문할 수 있는 정점이 여러 개인 경우에 정점 번호가 작은 것을 먼저 방문하기 위한 정렬

def bfs(graph, start):
    visited = [False for _ in range(N+1)]
    visited[0] = visited[start] = True
    route = [start]
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        for adj_node in graph[node]:
            if not visited[adj_node]:
                visited[adj_node] = True
                route.append(adj_node)
                queue.append(adj_node)
    return route

def dfs(graph, start, visited, route):
    if len(graph) - 1 == len(route):
        return route

    for node in graph[start]:
        if not visited[node]:
            visited[node] = True
            route.append(node)
            dfs(graph, node, visited, route)
    return route

visited = [False for _ in range(N+1)]
visited[0] = visited[V] = True

print(*dfs(graph, V, visited, [V]))
print(*bfs(graph, V))
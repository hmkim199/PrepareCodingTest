# https://www.acmicpc.net/problem/1167
# 트리의 지름

# 트리의 지름은 임의의 한 노드로부터 
# 가장 멀리있는 노드를 구해서, 
# 그 노드로부터 가장 멀리있는 노드까지의 거리가 트리의 지름.

V = int(input())
adjacent = [[] for _ in range(V+1)]
visited = [False for _ in range(V+1)]

# 시작 노드가 1부터 순서대로가 아닐 수도 있음. 이것 때문에 런타임 에러(RecursionError) 났었다.
for _ in range(V):
    info = list(map(int, input().split()))
    start_node = info[0]
    info = info[1:-1]
    node = 0
    dist = 0
    for j in range(len(info)):
        if j%2 == 0:
            node = info[j]
        else:
            dist = info[j]
            adjacent[start_node].append((node, dist)) # 어떤 노드가 거리 얼마인지

# print(adjacent)

def dfs(start, total_dist):
    # start 노드부터 가장 멀리 있는 노드와 거리 구하기
    global visited
    max_dist = total_dist
    farthest_node = start
    visited[start] = True
    for node, dist in adjacent[start]:
        if not visited[node]:
            visited[node] = True
            temp_node, temp_dist = dfs(node, total_dist+dist)
            if temp_dist > max_dist:
                max_dist = temp_dist
                farthest_node = temp_node

    # print(farthest_node, max_dist)
    return farthest_node, max_dist

farthest_node, max_dist = dfs(1, 0)
visited = [False for _ in range(V+1)]
# print()
farthest_node, max_dist = dfs(farthest_node, 0)
print(max_dist)
# https://www.acmicpc.net/problem/1389
# 케빈 베이컨의 6단계 법칙

# from collections import deque

# N, M = map(int, input())
# friends = [
#     set() for _ in range(N+1)
# ]

# for _ in range(M):
#     a, b = map(int, input().split())
#     friends[a].append(b)
#     friends[b].append(a)

# for i in range(N+1):
#     friends[i] = sorted(friends[i])

# kevin_nums = [0 for _ in range(N+1)]
# def bfs():
#     for i in range(1, N+1):
#         visited = [False for _ in range(N+1)]
#         queue = deque([i])
#         visited[i] = True
#         while queue:
#             user = queue.popleft()
#             for friend in friends[user]:
#                 if not visited[friend]:
#                     visited[friend] = True
#                     queue.append(friend)

# 그냥 bfs로는 거리 모름.... 다익스트라로 할까??? 아님 더 찾아볼까?
# 라는 생각 후 푼 방법 -> bfs + 백트래킹으로 최단 경로 구하기!
# 1의 케빈 베이컨 수 : dist(1, 1) + dist(1, 2) + dist(1, 3) + ... + dist(1, N)
# 각 노드의 케빈 베이컨 수를 위와 같은 방법으로 구해서 min index 출력

from collections import deque

N, M = map(int, input().split())
friends = [
    set() for _ in range(N+1)
]

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].add(b)
    friends[b].add(a)

for i in range(N+1):
    friends[i] = sorted(friends[i])

def bfs(i, j):
    """ i부터 j까지의 최단 경로(거리) 반환"""
    if i == j:
        return 0
    visited = [False for _ in range(N+1)]
    queue = deque([i])
    visited[i] = True
    predecessor = [None for _ in range(N+1)]
    while queue:
        user = queue.popleft()
        for friend in friends[user]:
            if not visited[friend]:
                visited[friend] = True
                queue.append(friend)
                predecessor[friend] = user

    distance = 0
    temp = j
    while temp:
        distance += 1
        temp = predecessor[temp]  # temp를 다음 노드로 바꿔준다
    return distance-1


kevin_nums = [0 for _ in range(N+1)]
# 1~N까지의 각각의 케빈 베이컨 수 구하기
for i in range(1, N+1):
    for j in range(1, N+1):
        kevin_nums[i] += bfs(i, j)

print(kevin_nums.index(min(kevin_nums[1:])))
# https://www.acmicpc.net/problem/1389
# 케빈 베이컨의 6단계 법칙

from collections import deque

N, M = map(int, input())
friends = [
    set() for _ in range(N+1)
]

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

for i in range(N+1):
    friends[i] = sorted(friends[i])

kevin_nums = [0 for _ in range(N+1)]
def bfs():
    for i in range(1, N+1):
        visited = [False for _ in range(N+1)]
        queue = deque([i])
        visited[i] = True
        while queue:
            user = queue.popleft()
            for friend in friends[user]:
                if not visited[friend]:
                    visited[friend] = True
                    queue.append(friend)

# 그냥 bfs로는 거리 모름.... 다익스트라로 할까??? 아님 더 찾아볼까?
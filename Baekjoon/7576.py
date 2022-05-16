# https://www.acmicpc.net/problem/7576
# 토마토

from collections import deque


M, N = map(int, input().split())
tomatoes = []
for _ in range(N):
    tomatoes.append(list(map(int, input().split())))


queue = deque()
empty = 0
result = 0

# bfs 시작 포인트 모두 삽입
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            queue.append((i, j))
        if tomatoes[i][j] == -1:
            empty += 1

# 모두 익어있는 게 아니면 bfs
if len(queue) + empty != N * M:
    while queue:
        x, y = queue.popleft()
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if x+dx < 0 or x+dx >= N or y+dy < 0 or y+dy >= M:
                continue
            # 최소 날짜 구하기 위해 토마토 밭 표기 -> 탐색 시작한 포인트의 토마토 표기 + 1
            if tomatoes[x+dx][y+dy] == 0:
                tomatoes[x+dx][y+dy] = tomatoes[x][y] + 1
                queue.append((x+dx, y+dy))

                # 토마토 밭 표기 -> 1부터 시작했으므로 tomatoes[x][y]+1이 아닌 tomatoes[x][y]
                result = tomatoes[x][y]
    
    # 0 하나라도 있으면 실패
    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 0:
                result = -1
print(result)
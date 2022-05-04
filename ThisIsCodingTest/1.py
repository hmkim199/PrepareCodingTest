# 음료수 얼려먹기

from collections import deque

N, M = map(int, input().split()) # 세로, 가로
ice = []
visited = [[False for _ in range(M)] for _ in range(N)]
dx = [0, 1, 0, -1] # 상 우 하 좌
dy = [1, 0, -1, 0] # 상 우 하 좌

for _ in range(N):
    ice.append(input().strip())

def bfs():
    global queue
    global visited
    while queue:
        i, j = queue.popleft()
        for direction in range(4):
            if 0 <= j+dx[direction] < M and 0 <= i+dy[direction] < N:
                if ice[i+dy[direction]][j+dx[direction]] == "0" and not visited[i+dy[direction]][j+dx[direction]]:
                    visited[i+dy[direction]][j+dx[direction]] = True
                    queue.append((i+dy[direction], j+dx[direction]))

queue = deque()
count = 0
for i in range(N):
    for j in range(M):
        if ice[i][j] == "0" and not visited[i][j]:
            queue.append((i, j))
            visited[i][j] = True
            bfs()
            count += 1

print(count)

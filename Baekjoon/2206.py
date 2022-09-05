# https://www.acmicpc.net/problem/2206
# 벽 부수고 이동하기

# 20퍼센트 대에서 틀렸습니다

from collections import deque


N, M = map(int, input().split())
matrix = []

for _ in range(N):
    matrix.append(list(map(int, list(input()))))


def bfs(matrix, M, N):
    minimum = 10e9
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[0][0] = True
    q = deque()
    q.append([0, 0, 1, False]) # x, y, 최단거리, 벽 부쉈는지
    while q:
        i, j, mini, is_crashed = q.popleft()
        if i == N-1 and j == M-1:
            minimum = min(minimum, mini)
            continue

        for dx, dy in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            x = i+dx
            y = j+dy
            if 0 <= x < N and 0 <= y < M:
                if matrix[x][y] == 0:
                    if not visited[x][y]:
                        visited[x][y] = True
                        q.append([x, y, mini+1, is_crashed])
                
                else:
                    if not is_crashed and not visited[x][y]:
                        visited[x][y] = True
                        q.append([x, y, mini+1, True])

    return minimum if minimum < 10e9 else -1

print(bfs(matrix, M, N))
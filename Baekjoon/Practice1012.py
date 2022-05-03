# https://www.acmicpc.net/problem/1012
# 유기농 배추

from collections import deque
import copy

T = int(input())

# BFS
# 인접 행렬로 구현

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(n, m):
    global q
    global visited    
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            if 0 <= x + dx[i] < n and 0 <= y + dy[i] < m:
                if matrix[x + dx[i]][y + dy[i]] == 1 and visited[x + dx[i]][y + dy[i]] == 0:
                    q.append((x + dx[i], y + dy[i]))
                    visited[x + dx[i]][y + dy[i]] = 1

for _ in range(T):
    # 행렬 초기화
    M, N, K = map(int, input().split())
    matrix = [[0 for _ in range(M)] for _ in range(N)]     # 배추 밭
    print(matrix)
    visited = copy.deepcopy(matrix)          # 방문 여부
    q = deque()
    count = 0

    # 배추 표시
    for i in range(K):
        y, x = map(int, input().split())
        matrix[x][y] = 1
    
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1 and visited[i][j] == 0:
                q.append((i, j))
                visited[i][j] = 1
                bfs(N, M)
                count += 1
    print(count)

        

                

# 인접 리스트로 구현
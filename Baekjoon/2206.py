# https://www.acmicpc.net/problem/2206
# 벽 부수고 이동하기

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
matrix = []

for _ in range(N):
    matrix.append(list(map(int, list(input().strip()))))


def bfs(matrix, M, N):
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1
    q = deque()
    q.append([0, 0, 0]) # x, y, 벽 부쉈는지
    while q:
        i, j, k = q.popleft()
        if i == N-1 and j == M-1:
            return visited[i][j][k]

        for dx, dy in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            x = i+dx
            y = j+dy
            if 0 <= x < N and 0 <= y < M and not visited[x][y][k]:
                if matrix[x][y] == 0:
                    visited[x][y][k] = visited[i][j][k] + 1
                    q.append([x, y, k])
                
                elif not k:
                    visited[x][y][1] = visited[i][j][k] + 1
                    q.append([x, y, 1])

    return -1

print(bfs(matrix, M, N))


# 한끝 차이인데 왜 틀렸을까
# # https://www.acmicpc.net/problem/2206
# # 벽 부수고 이동하기

# from collections import deque
# import sys

# input = sys.stdin.readline

# N, M = map(int, input().split())
# matrix = []

# for _ in range(N):
#     matrix.append(list(map(int, list(input().strip()))))


# def bfs(matrix, M, N):
#     visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
#     visited[0][0][0] = True
#     q = deque()
#     q.append([0, 0, 0]) # x, y, 벽 부쉈는지
#     while q:
#         i, j, k = q.popleft()
#         if i == N-1 and j == M-1:
#             return visited[i][j][k]

#         for dx, dy in ((1, 0), (-1, 0), (0, -1), (0, 1)):
#             x = i+dx
#             y = j+dy
#             if 0 <= x < N and 0 <= y < M:
#                 if matrix[x][y] == 0:
#                     if not visited[x][y][k]:
#                         visited[x][y][k] = visited[i][j][k] + 1
#                         q.append([x, y, k])
                
#                 else:
#                     if not k and not visited[x][y][k]:
#                         visited[x][y][1] = visited[i][j][k] + 1
#                         q.append([x, y, 1])

#     return -1

# print(bfs(matrix, M, N))
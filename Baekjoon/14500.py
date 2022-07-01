# https://www.acmicpc.net/problem/14500
# 테트로미노

# 시간 초과

# from collections import deque
# import copy


# N, M = map(int, input().split())
# matrix = []
# dir = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 오 위 아 왼
# maximum = 0
# for _ in range(N):
#     matrix.append(list(map(int, input().split())))

# for i in range(N):
#     for j in range(M):
#         queue = deque()
#         queue.append([(i, j)]) # 방문한 노드

#         while queue:
#             visited = queue.popleft()
#             if len(visited) >= 4:
#                 temp = 0
#                 for l, m in visited:
#                     temp += matrix[l][m]
#                 maximum = max(maximum, temp)
#                 continue

#             if len(visited) == 3 and (visited[0][0] == visited[1][0] == visited[2][0] or visited[0][1] == visited[1][1] == visited[2][1]):
#                 for k in range(len(dir)):
#                     x = visited[1][0] + dir[k][0]
#                     y = visited[1][1] + dir[k][1]
#                     if 0 <= x < N and 0 <= y < M and (x, y) not in visited:
#                         v = copy.deepcopy(visited)
#                         v.append((x, y))
#                         queue.append(v)

#             for k in range(len(dir)):
#                 x = visited[-1][0] + dir[k][0]
#                 y = visited[-1][1] + dir[k][1]
#                 if 0 <= x < N and 0 <= y < M and (x, y) not in visited:
#                     v = copy.deepcopy(visited)
#                     v.append((x, y))
#                     queue.append(v)

# print(maximum)


# 검색해서 풀었음 ㅠ dfs 공부 필요.. 솔직히 잘 모르겠음!!!! ㅠㅠㅠ

N, M = map(int, input().split())
matrix = []
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 오 위 아 왼
maximum = 0
visited = [[False for _ in range(M)] for _ in range(N)]

for _ in range(N):
    matrix.append(list(map(int, input().split())))

max_value = max(map(max, matrix))

def dfs(k, total, i, j):
    global maximum
    if k == 4:
        maximum = max(maximum, total)
        return
    
    if total + (4-k) * max_value <= maximum:
        return
    
    for dx, dy in dir:
        x, y = i+dx, j+dy

        if 0 <= x < N and 0 <= y < M and not visited[x][y]:
            visited[x][y] = True
            if k == 2:
                dfs(k+1, total + matrix[x][y], i, j)
            dfs(k+1, total + matrix[x][y], x, y)
            visited[x][y] = False

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(1, matrix[i][j], i, j)
        visited[i][j] = False

print(maximum)
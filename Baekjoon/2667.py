# https://www.acmicpc.net/problem/2667
# 단지번호붙이기

from collections import deque


N = int(input())
M = []
for _ in range(N):
    M.append(list(map(int, list(input()))))

visited = [[False for _ in range(N)] for _ in range(N)]
queue = deque()
apartment = []
for i in range(N):
    for j in range(N):
        if M[i][j] == 1 and not visited[i][j]:
            queue.append((i, j))
            visited[i][j] = True
            home = 1
            while queue:
                x, y = queue.popleft()
                for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    if x+dx < 0 or x+dx >= N or y+dy < 0 or y+dy >= N:
                        continue 
                    if M[x+dx][y+dy] == 1 and not visited[x+dx][y+dy]:
                        visited[x+dx][y+dy] = True
                        queue.append((x+dx, y+dy))
                        home += 1
            apartment.append(home)

print(len(apartment))
print(*sorted(apartment), sep='\n')
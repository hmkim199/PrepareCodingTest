# https://www.acmicpc.net/problem/2178
# 미로 탐색

from collections import deque


N, M = map(int, input().split())

maze = []
predecessor = [[[] for _ in range(M)] for _ in range(N)]
for _ in range(N):
    maze.append(list(map(int, list(input()))))

directions = [(1, 0), (0, -1), (-1, 0), (0, 1)] # 오른쪽 아래 왼쪽 위

queue = deque([(0, 0)])
predecessor[0][0] = None

while queue:
    x, y = queue.popleft()
    for dx, dy in directions:
        if 0 <= x + dx < N and 0 <= y + dy < M:
            if not predecessor[x+dx][y+dy] and maze[x+dx][y+dy] == 1:
                predecessor[x+dx][y+dy] = [x, y]
                queue.append((x+dx, y+dy))
                if x+dx == N-1 and y+dy == M-1:
                    queue = None
                    break

temp = [N-1, M-1]
distance = 1
while temp != [0, 0]:
    distance += 1
    temp = predecessor[temp[0]][temp[1]]
print(distance)
# https://www.acmicpc.net/problem/16236
# 아기 상어

# 예제 4번 통과 못 함. 답은 60이라는데 나는 56 나옴.

from collections import deque


N = int(input())
fish_tank = []
for _ in range(N):
    fish_tank.append(list(map(int, input().split())))

shark = 2
need_fish = shark
time = 0
target = [0 for _ in range(7)]
visited = [[False for _ in range(N)] for _ in range(N)]

# 아기 상어 위치 탐색 저장, 먹을 수 있는 물고기 정보 저장
for i in range(N):
    for j in range(N):
        if fish_tank[i][j] == 9:
            loc = [i, j]
            visited[i][j] = True
            fish_tank[i][j] = 0
        else:
            target[fish_tank[i][j]] += 1
    
queue = deque([[loc, time]])

while queue and sum(target[1:shark]) > 0:
     
    now, t = queue.popleft()

    for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        x = now[0]+dx
        y = now[1]+dy
        if x < 0 or x >= N or y < 0 or y >= N:
            continue
        if 0 < fish_tank[x][y] < shark and not visited[x][y]:
            target[fish_tank[x][y]] -= 1
            fish_tank[x][y] = 0
            visited[x][y] = True
            need_fish -= 1
            queue = deque()
            visited =  [[False for _ in range(N)] for _ in range(N)]
            visited[x][y] = True
            time = t+1
            queue.append([[x, y], t+1])

            if need_fish <= 0:
                shark += 1
                need_fish = shark
            break

        elif fish_tank[x][y] in (shark, 0) and not visited[x][y]:
            visited[x][y] = True
            queue.append([[x, y], t+1])
   
print(time)
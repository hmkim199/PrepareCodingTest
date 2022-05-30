# # https://www.acmicpc.net/problem/16236
# # 아기 상어

# # 이 풀이론 예제 4번 통과 못 함. 답은 60이라는데 나는 56 나옴.

# from collections import deque


# N = int(input())
# fish_tank = []
# for _ in range(N):
#     fish_tank.append(list(map(int, input().split())))

# shark = 2
# need_fish = shark
# time = 0
# target = [0 for _ in range(7)]
# visited = [[False for _ in range(N)] for _ in range(N)]

# # 아기 상어 위치 탐색 저장, 먹을 수 있는 물고기 정보 저장
# for i in range(N):
#     for j in range(N):
#         if fish_tank[i][j] == 9:
#             loc = [i, j]
#             visited[i][j] = True
#             fish_tank[i][j] = 0
#         else:
#             target[fish_tank[i][j]] += 1
    
# queue = deque([[loc, time]])

# # 먹을 수 있는 물고기를 따로 저장해서 거리 우선순위 조건 확인하고 먹기
# while queue and sum(target[1:shark]) > 0:
#     queue
#     now, t = queue.popleft()

#     for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
#         x = now[0]+dx
#         y = now[1]+dy
#         if x < 0 or x >= N or y < 0 or y >= N:
#             continue
#         if 0 < fish_tank[x][y] < shark and not visited[x][y]:
#             target[fish_tank[x][y]] -= 1
#             fish_tank[x][y] = 0
#             visited[x][y] = True
#             need_fish -= 1
#             queue = deque()
#             visited =  [[False for _ in range(N)] for _ in range(N)]
#             visited[x][y] = True
#             time = t+1
#             queue.append([[x, y], t+1])

#             if need_fish <= 0:
#                 shark += 1
#                 need_fish = shark
#             break

#         elif fish_tank[x][y] in (shark, 0) and not visited[x][y]:
#             visited[x][y] = True
#             queue.append([[x, y], t+1])
   
# print(time)




# ========================================================================================

# https://www.acmicpc.net/problem/16236
# 아기 상어

# 풀리긴 했지만 시간 초과.. -> pypy로 통과됨!!! => python 으로 통과한 사람들도 있어서 더 생각해보면 좋을듯.

from collections import deque


N = int(input())
fish = []
for _ in range(N):
    fish.append(list(map(int, input().split())))

shark = 2
need_fish = shark
time = 0
target = [set() for _ in range(7)]
loc = (0, 0)

# 아기 상어 위치 탐색 저장, 먹을 수 있는 물고기 정보 저장
for i in range(N):
    for j in range(N):
        if fish[i][j] == 9:
            loc = [i, j]
            fish[i][j] = 0
        elif fish[i][j] > 0:
            target[fish[i][j]].add((i, j))

# 각 목표물까지의 거리가 얼마인지 확인(bfs)
def bfs(target_x, target_y):
    global loc
    visited = [[False for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append([loc, 0])
    dist = 10e9
    while q:
        now, t = q.popleft()
        if now[0] == target_x and now[1] == target_y:
            dist = t
            break
        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            x = now[0]+dx
            y = now[1]+dy
            if x < 0 or x >= N or y < 0 or y >= N:
                continue
            if fish[x][y] <= shark and not visited[x][y]:
                visited[x][y] = True
                q.append([(x, y), t+1])
    
    if dist == 10e9:
        return -1
    return dist 


def find_target():
    # 지금 상어보다 작은 애들 위치 모두 보면서 거리 재기 가장 가까우면서 위, 왼쪽인 애 리턴 -> sort
    options = []
    if shark > 7:
        limit = 7
    else:
        limit = shark
    for i in range(1, limit):
        if len(target[i]) <= 0:
            continue
        for x, y in target[i]:
            dist = bfs(x, y)
            if dist == -1:
                continue
            options.append([(x, y), dist])
    if len(options) == 0:
        return -1, -1
    options.sort(key=lambda x: (x[1], x[0]))
    return options[0]

# 먹기
# 또 거리 확인
def eat():
    global time
    global loc
    global shark
    global need_fish
    options = 0
    for i in range(1, 7):
        options += len(target[i])
    while options > 0:
        now, t = find_target()
        if now == -1 and t == -1:
            return time
        time += t
        loc = now
        need_fish -= 1
        target[fish[now[0]][now[1]]].discard(now)
        fish[now[0]][now[1]] = 0

        if need_fish == 0:
            shark += 1
            need_fish = shark

    return time

print(eat())
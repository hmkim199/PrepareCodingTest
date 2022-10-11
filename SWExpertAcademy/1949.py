# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq&categoryId=AV5PoOKKAPIDFAUq&categoryType=CODE&problemTitle=%EB%AA%A8%EC%9D%98+SW&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 1949. [모의 SW 역량테스트] 등산로 조성

# k만큼 깎을 수 있는 걸 까먹었지만 다시 풀었음! 1시간 30분 조금 넘게 걸림.

from collections import deque
from copy import deepcopy


T = int(input())
for testcase in range(1, T+1):
    N, K = map(int, input().split())
    top = 0 # 봉우리
    matrix = []
    for _ in range(N):
        line = list(map(int, input().split()))
        top = max(top, max(line))
        matrix.append(line)
    
    q = deque()
    # 최대 값 찾기.
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == top:
                q.append([(i, j), top, False, set([(i, j)])])
    
    depth = 0
    while q:
        pos, num, cut, visited = q.popleft()
        depth = max(depth, len(visited))
        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            x = pos[0]+dx
            y = pos[1]+dy

            if 0 <= x < N and 0 <= y < N and (x, y) not in visited:
                if matrix[x][y] < num:
                    new_visited = deepcopy(visited)
                    new_visited.add((x, y))
                    q.append([(x, y), matrix[x][y], cut, new_visited])
                elif not cut:
                    if matrix[x][y] - K < num:
                        new_visited = deepcopy(visited)
                        new_visited.add((x, y))
                        q.append([(x, y), num-1, not cut, new_visited])
    print("#" + str(testcase), str(depth))
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PoOKKAPIDFAUq&categoryId=AV5PoOKKAPIDFAUq&categoryType=CODE&problemTitle=%EB%AA%A8%EC%9D%98+SW&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 1949. [모의 SW 역량테스트] 등산로 조성

# k만큼 깎을 수 있는 걸 까먹었지만 다시 풀었음! 1시간 30분 조금 넘게 걸림.

from collections import deque
from copy import deepcopy


T = int(input())
for testcase in range(1, T+1):
    N, K = map(int, input().split())
    top = 0 # 봉우리 높이
    matrix = []
    for _ in range(N):
        line = list(map(int, input().split()))
        top = max(top, max(line))
        matrix.append(line)
    
    q = deque()
    # 최대 값 찾아서 큐에 넣기.
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == top:
                q.append([(i, j), top, False, set([(i, j)])]) # 봉우리 위치, 높이, 아직 깎이지 않음(False), visited 
    
    depth = 0
    while q:
        pos, num, cut, visited = q.popleft()
        depth = max(depth, len(visited)) # 가장 깊은 깊이 최신화
        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)): # 위 아래 오른쪽 왼쪽 
            x = pos[0]+dx # 탐색할 x 위치
            y = pos[1]+dy # 탐색할 y 위치

            if 0 <= x < N and 0 <= y < N and (x, y) not in visited: # 지도 내에 있고 아직 방문하지 않은 경우
                if matrix[x][y] < num: # 이전 숫자보다 새 숫자가 작으면 큐에 넣기.
                    new_visited = deepcopy(visited)
                    new_visited.add((x, y))
                    q.append([(x, y), matrix[x][y], cut, new_visited])
                elif not cut: # 이전 숫자보다 새 숫자가 크거나 같으면
                    if matrix[x][y] - K < num: # K 범위 내에서 깎았을 때 이전 숫자보다 작아지면 큐에 넣기.
                        new_visited = deepcopy(visited)
                        new_visited.add((x, y))
                        q.append([(x, y), num-1, not cut, new_visited])
    print("#" + str(testcase), str(depth))
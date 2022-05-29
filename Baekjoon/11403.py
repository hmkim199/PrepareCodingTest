# https://www.acmicpc.net/problem/11403
# 경로 찾기


# 시간 초과 때문에 visited를 설정해줘야 하는데, 어디서, 어떻게 얼마나 무슨 변수에 대해 방문 처리를 해야하는지 몰랐다.
# 처음에는 visited를 adj 딥카피로 2차원 배열로 하기도 하고 -> 완전 쓸데없는 짓
# 나중에는 검색을 조금 해보다가 1차원 배열로 체크할 수 있다는 것을 알았다.
# 그 다음엔 도움을 받아 어디서 1차원 배열로 써야하는지 알게 됐는데, 무슨 변수에 대해 방문 체크를 해줘야하는지를 몰라서 바보같이 한참을 풀었다. 결국 풀었지만 찝찝함이 남았다. 다시 풀자 꼭. 

from collections import deque
from copy import deepcopy


N = int(input())
adj = []

for _ in range(N):
    adj.append(list(map(int, input().split())))

answer = deepcopy(adj)

for i in range(N):
    for j in range(N):
        if adj[i][j] == 1:
            visited = [False] * N
            queue = deque()
            visited[j] = True  # 큐에 넣을 친구를 방문 처리 해줘야 함!!!
            queue.append(j)
            while queue:
                now = queue.popleft()
                for k in range(N):
                    if adj[now][k] == 1 and now != i and not visited[k]:
                        answer[i][k] = 1
                        visited[k] = True  # 큐에 넣을 친구 방문 처리
                        queue.append(k)

for i in range(N):
    print(*answer[i])
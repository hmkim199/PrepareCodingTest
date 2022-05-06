# https://www.acmicpc.net/problem/1697
# 숨바꼭질 

from collections import deque


N, K = map(int, input().split())
MAX_LOCATION = 100000

def bfs(N, K):
    if N == K:
        return 0
    queue = deque([N])
    predecessor = {N: None}
    while queue:
        now = queue.popleft()
        possible_loc = [now-1, now+1, now*2]
        for loc in possible_loc:
            # loc 범위 체크해주지 않으면 메모리 초과
            if loc not in predecessor and 0 <= loc <= MAX_LOCATION:
                predecessor[loc] = now
                queue.append(loc)
                if loc == K:
                    queue = None
                    break

    temp = K
    minute = 0
    while temp is not None: # while temp로 하면 0인 경우에도 반복문 수행하지 않아서 오답!!
        minute += 1
        temp = predecessor.get(temp)
    return minute - 1

print(bfs(N, K))
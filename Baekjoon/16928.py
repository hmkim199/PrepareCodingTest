# https://www.acmicpc.net/problem/16928
# 뱀과 사다리 게임

from collections import deque
import sys

N, M = map(int, input().split())
board = [i for i in range(101)]
visited = [False for _ in range(101)]
visited[0] = visited[1] = True
dest = 100

for _ in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    board[x] = y

for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    board[u] = v

# 첫 번째 사다리 만나기 전까진 일반 주사위.
# 9퍼에서 틀렸습니다

def bfs():
    queue = deque()
    queue.append([1, 0])
    while queue:
        now, cnt = queue.popleft()
        temp = now
        for i in range(1, 7):
            if not visited[now+i]:
                if now+i < dest:
                    visited[now+i] = True
                    if board[now+i] > now+i:
                        visited[board[now+i]] = True
                        queue.append([board[now+i], cnt+1])
                    elif board[now+i] == now+i:
                        temp = now+i
                elif now+i == dest:
                    return cnt+1
                # 뱀 타는게 이득인 경우. 이거 생각해서 고치기
                # else:
                #     queue.append([board[now+i], cnt+1])
        queue.append([temp, cnt+1])
    return -1

print(bfs())

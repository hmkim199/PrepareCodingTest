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

# 현재 위치에서 주사위 1~6이 나왔을 때 각각을 사다리인 경우, 뱀인 경우에 큐에 추가. 일반 칸인 경우에는 일반 칸 중 가장 큰 수만 큐에 추가.
def bfs():
    queue = deque()
    queue.append([1, 0])
    while queue:
        now, cnt = queue.popleft()
        local_max = now # 일반 칸 중 가장 큰 수

        # 현 위치에서 주사위 숫자 1~6의 경우의 수
        for i in range(1, 7):
            if not visited[now+i]:
                if now+i < dest:
                    visited[now+i] = True
                    # 사다리인 경우
                    if board[now+i] > now+i:
                        visited[board[now+i]] = True
                        queue.append([board[now+i], cnt+1])
                    
                    # 일반 칸
                    elif board[now+i] == now+i:
                        local_max = now+i
                    
                    # 뱀 타는게 이득인 경우.
                    else:
                        visited[board[now+i]] = True
                        queue.append([board[now+i], cnt+1])
                elif now+i == dest:
                    return cnt+1
                
        queue.append([local_max, cnt+1])
    return -1

print(bfs())

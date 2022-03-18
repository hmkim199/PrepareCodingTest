# https://www.acmicpc.net/problem/10866
# 덱

from collections import deque
import sys

N = int(input())
d = deque()

for _ in range(N):
    op = sys.stdin.readline().strip().split()
    if op[0] == "push_back":
        d.append(int(op[1]))
    elif op[0] == "push_front":
        d.appendleft(int(op[1]))
    elif op[0] == "front":
        print(d[0]) if d else print(-1)
    elif op[0] == "back":
        print(d[-1]) if d else print(-1)
    elif op[0] == "pop_front":
        print(d.popleft()) if d else print(-1)
    elif op[0] == "pop_back":
        print(d.pop()) if d else print(-1)
    elif op[0] == "size":
        print(len(d))
    elif op[0] == "empty":
        print(0) if d else print(1)


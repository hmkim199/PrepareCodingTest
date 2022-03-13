# https://www.acmicpc.net/problem/10845
# 큐


from collections import deque
import sys

N = int(sys.stdin.readline().strip())
q = deque()

for _ in range(N):
    op = sys.stdin.readline().strip().split()

    if op[0] == "push":
        q.append(int(op[1]))
    elif op[0] == "pop":
        print(q.popleft()) if q else print(-1)
    elif op[0] == "size":
        print(len(q))
    elif op[0] == "empty":
        print(0) if q else print(1)
    elif op[0] == "front":
        print(q[0]) if q else print(-1)
    elif op[0] == "back":
        print(q[-1]) if q else print(-1)
# https://www.acmicpc.net/problem/10828
# 스택

# input으로 하면 안 됨.

import sys

N = int(sys.stdin.readline().strip())
s = []

for _ in range(N):
    op = sys.stdin.readline().strip().split()

    if op[0] == "push":
        s.append(int(op[1]))
    elif op[0] == "pop":
        print(s.pop()) if len(s) > 0 else print(-1)
    elif op[0] == "size":
        print(len(s))
    elif op[0] == "empty":
        print(0) if s else print(1)
    elif op[0] == "top":
        print(s[-1]) if s else print(-1) 

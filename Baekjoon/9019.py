# https://www.acmicpc.net/problem/9019
# DSLR

# 시간 초과!!!
from collections import deque


T = int(input())
result = []

for _ in range(T):
    A, B = map(int, input().split())

    if A == B:
        print("")
        continue

    queue = deque()
    visited = set()
    queue.append([A, ""])
    visited.add(A)
    found = False
    while queue and not found:
        temp, operations = queue.popleft()
        DSLR = []
        dic = {0:"D", 1:"S", 2:"L", 3:"R"}
        DSLR.append(temp * 2 % 10000)
        DSLR.append(temp - 1 if temp != 0 else 9999)
        temp = str(temp)
        if len(temp) < 4:
            temp = "0" * (4 - len(temp)) + temp
        DSLR.append(int(temp[1:]+temp[0]))
        DSLR.append(int(temp[3]+temp[0:3]))
        for i in range(4):
            if DSLR[i] == B:
                result.append(operations+dic[i])
                found = True
                break
            queue.append([DSLR[i], operations+dic[i]])
            visited.add(DSLR[i])

print(*result, sep="\n")
        
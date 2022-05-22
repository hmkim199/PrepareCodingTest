# https://www.acmicpc.net/problem/9019
# DSLR

# pypy로 통과. python 은 시간초과
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
        DSLR.append(temp%1000*10+temp//1000)
        DSLR.append(temp%10*1000+temp//10)
        for i in range(4):
            if DSLR[i] == B:
                result.append(operations+dic[i])
                found = True
                break
            if DSLR[i] not in visited:
                queue.append([DSLR[i], operations+dic[i]])
                visited.add(DSLR[i])

print(*result, sep="\n")
        
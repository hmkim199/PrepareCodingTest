# https://www.acmicpc.net/problem/1927
# 최소 힙

import sys
import heapq

heap = []
result = []

N = int(input())
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x > 0:
        heapq.heappush(heap, x)
    elif x == 0:
        res = 0
        if heap:
            res = heapq.heappop(heap)
        result.append(res)

print(*result, sep="\n")
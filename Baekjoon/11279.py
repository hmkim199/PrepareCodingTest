# https://www.acmicpc.net/problem/11279
# 최대 힙

import heapq
import sys

heap = []
result = []

N = int(input())
for _ in range(N):
    op = int(sys.stdin.readline().strip())
    if op > 0:
        heapq.heappush(heap, -op)
    elif op == 0:
        if heap:
            res = -heapq.heappop(heap)
        else:
            res = 0
        result.append(res)

print(*result, sep="\n")
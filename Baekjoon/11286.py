# https://www.acmicpc.net/problem/11286
# 절댓값 힙

import heapq
import sys

heap = []
N = int(input())
result = []

for _ in range(N):
    op = int(sys.stdin.readline().strip())
    if op != 0:
        heapq.heappush(heap, (abs(op), op))
    else:
        if heap:
            res = heapq.heappop(heap)[1]
        else:
            res = 0
        result.append(res)

print(*result, sep="\n")
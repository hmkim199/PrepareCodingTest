# https://www.acmicpc.net/problem/7662
# 이중 우선순위 큐

import heapq
import sys

T = int(input())

for _ in range(T):
    K = int(input())
    min_heap = []
    max_heap = []
    deleted = [False for _ in range(K)]

    for i in range(K):    
        op, n = sys.stdin.readline().strip().split()
        n = int(n)

        if op == 'I':
            heapq.heappush(min_heap, (n, i))
            heapq.heappush(max_heap, (-n, i))
        
        elif op == 'D':
            if n == 1:
                while max_heap and deleted[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    deleted[max_heap[0][1]] = True
                    heapq.heappop(max_heap)
            if n == -1:
                while min_heap and deleted[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    deleted[min_heap[0][1]] = True
                    heapq.heappop(min_heap)
    
    is_empty = True
    res = [0, 0]
    while max_heap and deleted[max_heap[0][1]]:
        heapq.heappop(max_heap)
    if max_heap:
        res[0] = heapq.heappop(max_heap)
        is_empty = False
    
    while min_heap and deleted[min_heap[0][1]]:
        heapq.heappop(min_heap)
    if min_heap:
        res[1] = heapq.heappop(min_heap)
        is_empty = False
    
    if is_empty:
        print('EMPTY')
    else:
        print(-res[0][0], res[1][0])
    
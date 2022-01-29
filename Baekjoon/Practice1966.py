# https://www.acmicpc.net/problem/1966
# 프린터 큐

from collections import deque

testcases = int(input())
result = []
for _ in range(testcases):
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    indexed_importance = deque()
    count = 0
    for i in range(len(importance)):
        l = [i, importance[i]]
        indexed_importance.append(l)
    while True:
        priority = max(indexed_importance, key=lambda x: x[1])[1]
        if indexed_importance[0][1] == priority:
            p = indexed_importance.popleft()
            count += 1
            if p[0] == M:
                result.append(count)
                break
        else:
            indexed_importance.append(indexed_importance.popleft())

print(*result, sep="\n")
# https://www.acmicpc.net/problem/10773
# 제로

import sys

K = int(input())

nums = []
for _ in range(K):
    i = int(sys.stdin.readline().strip())
    if i == 0:
        nums.pop()
    else:
        nums.append(i)

print(sum(nums))


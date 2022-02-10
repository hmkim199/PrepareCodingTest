# https://www.acmicpc.net/problem/2751
# 수 정렬하기 2

import sys

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()
print(*nums, sep="\n")
# https://www.acmicpc.net/problem/10989
# 수 정렬하기 3

from os import sep
import sys

N = int(input())
nums = [i+1 for i in range(10001)]
d = {}
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if num in d:
        d[num] += 1
    else: 
        d[num] = 1

for item in sorted(d.items()):
    for _ in range(item[1]):
        print(item[0])

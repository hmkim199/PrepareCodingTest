# https://www.acmicpc.net/problem/17219
# 비밀번호 찾기

import sys

N, M = map(int, input().split())
memo = {}
for _ in range(N):
    site, pw = sys.stdin.readline().strip().split()
    memo[site] = pw

for _ in range(M):
    site = sys.stdin.readline().strip().strip()
    print(memo[site])
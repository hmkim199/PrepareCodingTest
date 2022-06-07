# https://www.acmicpc.net/problem/1620
# 나는야 포켓몬 마스터 이다솜

import sys

N, M = map(int, sys.stdin.readline().strip().split())

poketmon = {}
for i in range(N):
    p = sys.stdin.readline().strip()
    poketmon[p] = i+1
    poketmon[str(i+1)] = p

ans = []
for _ in range(M):
    ans.append(poketmon[sys.stdin.readline().strip()])
    # print(poketmon[input()])

print(*ans, sep='\n')
# https://www.acmicpc.net/problem/1764
# 듣보잡

import sys

N, M = map(int, input().split())
never_heard = set()
never_seen = set()

for _ in range(N):
    never_heard.add(sys.stdin.readline().rstrip())

for _ in range(N):
    never_seen.add(sys.stdin.readline().rstrip())

both = list(sorted(never_heard & never_seen))

print(len(both))
print(*both, sep="\n")
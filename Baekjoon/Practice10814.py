# https://www.acmicpc.net/problem/10814
# 나이순 정렬

N = int(input())
members = []

for _ in range(N):
    members.append(input().split())

members.sort(key=lambda x: int(x[0]))

for li in members:
    print(*li)
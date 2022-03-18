# https://www.acmicpc.net/problem/11651
# 좌표 정렬하기 2

N = int(input())
points = []

for _ in range(N):
    point = list(map(int, input().split()))
    points.append(point)

points.sort(key=lambda x: (x[1], x[0]))

for p in points:
    print(*p)
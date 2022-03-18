# https://www.acmicpc.net/problem/11650
# 좌표 정렬하기

N = int(input())

points = []
for _ in range(N):
    point = list(map(int, input().split()))
    points.append(point)

points.sort(key=lambda x: (x[0], x[1]))

for p in points:
    print(*p)
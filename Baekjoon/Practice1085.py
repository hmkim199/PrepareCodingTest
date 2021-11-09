# https://www.acmicpc.net/problem/1085
# 직사각형에서 탈출

x, y, w, h = map(int, input().split())

dist = [abs(w-x), abs(0-x), abs(h-y), abs(0-y)]

print(min(dist))
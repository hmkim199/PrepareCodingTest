# 
# 

import sys

N, M, B = map(int, sys.stdin.readline().split())

# 블록제거 2초, 쌓기 1초
ground = []
for _ in range(N):
    ground.append(list(map(int, sys.stdin.readline().split())))

min_time, min_height = 9223372036854775807, 0
for height in range(257):
    bottom = top = 0
    for i in range(N):
        for j in range(M):
            if ground[i][j] < height:
                bottom += height-ground[i][j]
            else:
                top += ground[i][j]-height
    if bottom > top + B:
        continue
    time = bottom + top*2
    if time <= min_time:
        min_time = time
        min_height = height
print(min_time, min_height)

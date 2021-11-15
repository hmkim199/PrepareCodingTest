# https://www.acmicpc.net/problem/2292
# 벌집

N = int(input())

now = 1
min_room = 1
while now < N:
    now += 6*min_room
    min_room += 1
print(min_room)


# https://www.acmicpc.net/problem/2292
# 벌집

# 저번 풀이
N = int(input())

now = 1
min_room = 1
while now < N:
    now += 6*min_room
    min_room += 1
print(min_room)

# 이번 풀이
N = int(input())
room = 1
count = 1
shape = 6
while room < N:
    if room + shape * count <= N:
        room += shape * count
    else:
        room = N
    count += 1

print(count)







# https://www.acmicpc.net/problem/1654
# 랜선 자르기

K, N = map(int, input().split())
lines = []

for _ in range(K):
    lines.append(int(input()))

length = sum(lines)//K

while True:
    count = 0
    for line in lines:
        count += line // length
    if count >= N:
        break
    length -= 1

print(length)
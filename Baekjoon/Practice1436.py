# https://www.acmicpc.net/problem/1436
# 영화감독 숌

N = int(input())

cnt = 1
num = 666

while cnt < N:
    num += 1
    if "666" in str(num):
        cnt += 1

print(num)
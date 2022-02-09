# https://www.acmicpc.net/problem/2231
# 분해합

N = int(input())
creator = 0
for i in range(1, N):
    li = [i] + list(str(i))
    li = [int(i) for i in li]
    if sum(li) == N:
        creator = li[0]
        break
print(creator)
    
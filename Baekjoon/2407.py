# https://www.acmicpc.net/problem/2407
# 조합

n, m = map(int, input().split())

m = min(m, n-m)
answer = 1
for i in range(n, n-m, -1):
    answer *= i

for i in range(1, m+1):
    answer //= i

print(answer)
# https://www.acmicpc.net/problem/11050
# 이항 계수 1

N, K = map(int, input().split())

result = 1
for i in range(K):
    result *= (N-i)
for i in range(K, 0, -1):
    result /= i

print(int(result))
# https://www.acmicpc.net/problem/11050
# 이항 계수 1

# N, K = map(int, input().split())

# result = 1
# for i in range(K):
#     result *= (N-i)
# for i in range(K, 0, -1):
#     result /= i

# print(int(result))


# int로 감싸지 않으면 틀림.
# 지금 풀이

N, K = map(int, input().split())

res = 1
for i in range(N-K):
    res *= (N-i)
for i in range(N-K, 0, -1):
    res /= i

print(int(res))
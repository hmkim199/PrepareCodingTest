# https://www.acmicpc.net/problem/9095
# 1, 2, 3 더하기

T = int(input())
dp = [0 for i in range(11)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-3]+dp[i-2]+dp[i-1]

for _ in range(T):
    n = int(input())
    print(dp[n])
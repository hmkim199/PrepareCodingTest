# https://www.acmicpc.net/problem/2579
# 계단 오르기


num = int(input())
stairs = []
for _ in range(num):
    stairs.append(int(input()))

dp = [0 for i in range(num)]
dp[0] = stairs[0]
if num > 1:
    dp[1] = stairs[0]+stairs[1]
if num > 2:
    dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])
for i in range(3, num):
    dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i])

print(dp[-1])
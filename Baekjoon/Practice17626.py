# https://www.acmicpc.net/problem/17626
# Four Squares


# 틀린 풀이
# n = int(input())
# cnt = 0
# while n > 0:
#     temp = int(n**0.5)
#     print(temp)
#     n -= temp**2
#     cnt += 1
# print(cnt)


# 규칙 -> 루트 값이 정수면 1, 그 외에는 dp(i) = min(dp(i-1)+dp(1), dp(i-2)+dp(2), ...)
# 틀린 풀이 -> 너무 느림
# n = int(input())
# dp = [4 for i in range(n+1)]
# for i in range(1, n+1):
#     if i**0.5 == int(i**0.5):
#         dp[i] = 1
#     else:
#         for j in range(1, i//2+1):
#             temp = dp[j]+dp[i-j]
#             if dp[i] > temp:
#                 dp[i] = temp
# print(dp[n])


# 규칙 -> 루트 값이 정수면 1, 그 외에는 dp(i) = min(dp(i-j*j)+1) -> j는 1부터~
# pypy3으로 통과
n = int(input())
dp = [4 for i in range(n+1)]
for i in range(1, n+1):
    if i**0.5 == int(i**0.5):
        dp[i] = 1
    else:
        for j in range(int(i**0.5), 0, -1):
            if dp[i] == 2: break
            dp[i] = min(dp[i-j*j]+1, dp[i])
print(dp[n])
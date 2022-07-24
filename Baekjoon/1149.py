# https://www.acmicpc.net/problem/1149
# RGB거리

# 검색해서 풂.
N = int(input())
cost = []
for _ in range(N):
    cost.append(list(map(int, input().split())))

dp = [cost[0]]
for i in range(1, N):
    total = [0, 0, 0]
    total[0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    total[1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    total[2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
    dp.append(total)

print(min(dp[-1]))

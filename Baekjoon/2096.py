# https://www.acmicpc.net/problem/2096
# 내려가기

# 메모리초과

import copy

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
    
min_dp = copy.deepcopy(arr)

for i in range(1, N):
    j = 0
    arr[i][j] += max(arr[i-1][j], arr[i-1][j+1])
    min_dp[i][j] += min(min_dp[i-1][j], min_dp[i-1][j+1])
    
    j = 1
    arr[i][j] += max(arr[i-1][j-1], arr[i-1][j], arr[i-1][j+1])
    min_dp[i][j] += min(min_dp[i-1][j-1], min_dp[i-1][j], min_dp[i-1][j+1])

    j = 2
    arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
    min_dp[i][j] += min(min_dp[i-1][j-1], min_dp[i-1][j])


print(max(arr[-1]), min(min_dp[-1]))

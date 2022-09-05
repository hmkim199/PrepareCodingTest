# https://www.acmicpc.net/problem/2096
# 내려가기

# input함수 그대로 쓰면 시간초과 나서 readline쓰기

import copy
import sys

input = sys.stdin.readline

N = int(input())
max_dp = [0, 0, 0]
min_dp = [0, 0, 0]
for i in range(N):
    arr = list(map(int, input().split()))
    if i == 0:
        for j in range(3):
            max_dp[j] = arr[j]
            min_dp[j] = arr[j]
        continue

    temp = [0, 0, 0]
    temp[0] = max(max_dp[:2]) + arr[0]
    temp[1] = max(max_dp) + arr[1]
    temp[2] = max(max_dp[1:]) + arr[2]

    max_dp = copy.deepcopy(temp)

    temp = [0, 0, 0]
    temp[0] = min(min_dp[:2]) + arr[0]
    temp[1] = min(min_dp) + arr[1]
    temp[2] = min(min_dp[1:]) + arr[2]
    min_dp = copy.deepcopy(temp)

print(max(max_dp), min(min_dp))
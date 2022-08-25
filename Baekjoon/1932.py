# https://www.acmicpc.net/problem/1932
# 정수 삼각형

# dp 공부 더하기ㅠ 생각이 나질 않아~

import sys
input = sys.stdin.readline

n = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]

# 입력
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        dp[i][j] = temp[j]

for i in range(n-2, -1, -1): # 제일 마지막 줄 - 1 줄부터 위로 올라가면서 업데이트
    for j in range(n-1):
        dp[i][j] += max(dp[i+1][j], dp[i+1][j+1]) # 기존 값 + 양 대각선 중 max 값

print(max(dp[0]))
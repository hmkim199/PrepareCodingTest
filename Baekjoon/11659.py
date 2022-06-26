# https://www.acmicpc.net/problem/11659
# 구간 합 구하기 4

# 시간 초과. 슬라이싱도 시간 초과

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# nums = list(map(int, input().split()))

# result = []

# for _ in range(M):
#     i, j = map(int, input().split())
#     temp = 0
#     for k in range(i-1, j):
#         temp += nums[k]
#     result.append(temp)

# print(*result, sep="\n")

# import sys
# input = sys.stdin.readline().rstrip

# N, M = map(int, input().split())
# nums = list(map(int, input().split()))

# result = {}

# for i in range(N):
#     temp = 0
#     for j in range(i+1, N):
#         temp += nums[j]
#         result[(i+1, j+1)] = temp


# for _ in range(M):
#     i, j = map(int, input().split())
#     if i == j:
#         print(nums[i-1])
#     else:
#         print(result[(i, j)])


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

accumulate_sum = {0: 0}
result = []

temp = 0
for i in range(N):
    temp += nums[i]
    accumulate_sum[i+1] = temp

for _ in range(M):
    i, j = map(int, input().split())
    res = accumulate_sum[j] - accumulate_sum[i-1]
    result.append(res)

print(*result, sep="\n")
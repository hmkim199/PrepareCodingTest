# https://www.acmicpc.net/problem/2798
# 블랙잭

N, M = map(int, input().split())
nums = list(map(int, input().split()))

total = []
length = len(nums)
for i in range(length-2):
    for j in range(i+1, length-1):
        for k in range(j+1, length):
            temp = nums[i] + nums[j] + nums[k]
            if temp <= M:
                total.append(temp)

print(max(total))
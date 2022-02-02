# https://www.acmicpc.net/problem/2164
# 카드2

# 시간 초과
# N = int(input())
# nums = [i+1 for i in range(N)]

# while len(nums) > 1:
#     nums.pop(0)
#     nums.append(nums.pop(0))
# print(nums[0])

# 시간 초과
# N = int(input())
# nums = [i+1 for i in range(N)]

# while len(nums) > 1:
#     nums = nums[2:]+[nums[1]]
# print(nums[0])


N = int(input())
nums = [i+1 for i in range(N)]
idx = 0

while len(nums) - idx > 1:
    idx += 1
    nums.append(nums[idx])
    idx += 1

print(nums[idx])


# https://www.acmicpc.net/problem/3052
# 나머지 

nums = []

for _ in range(10):
    num = int(input())
    nums.append(num%42)

print(len(set(nums)))
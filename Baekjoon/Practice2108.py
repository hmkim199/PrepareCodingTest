# https://www.acmicpc.net/problem/2108
# 통계학
import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline().strip()))

nums.sort()
def average(nums):
    return round(sum(nums)/len(nums))

def center(nums):
    return nums[len(nums)//2]

def freq(nums):
    count = Counter(nums).most_common(2)
    if len(count)>1:
        if count[1][1] == count[0][1]:
            return count[1][0]
    return count[0][0]

def between(nums):
    return nums[-1]-nums[0]

print(average(nums))
print(center(nums))
print(freq(nums))
print(between(nums))
        
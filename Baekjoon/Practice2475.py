# 일리스 알고리즘 스터디 4주차

# https://www.acmicpc.net/problem/2475
# 검증수

# nums = list(map(int, input().split()))
# nums = [x**2 for x in nums]
# print(sum(nums)%10)

# ===============================================
# https://www.acmicpc.net/problem/2557
# Hello World

# print("Hello World!")

# ===============================================
# https://www.acmicpc.net/problem/2562
# 최댓값

# 예전 풀이
nums = []
for i in range(9):
    nums.append(int(input()))
    
maximum = max(nums)

print(maximum)
print(nums.index(maximum)+1)

# 이번 풀이
I = 9
d = {}
for i in range(I):
    d[i+1] = int(input())
print(max(d.values()))
print(max(d, key=d.get))
# print(max(d.keys(), key=lambda k: d[k]))


# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 타겟 넘버


def dfs(numbers, target, now):
    if not numbers:
        if now == target:
            return 1
        else:
            return 0
    return dfs(numbers[1:], target, now + numbers[0]) + dfs(numbers[1:], target, now - numbers[0])
    

def solution(numbers, target):
    return dfs(numbers, target, 0)

print(solution([1, 1, 1, 1, 1], 3)) # 5
print(solution([4, 1, 2, 1], 4)) # 2

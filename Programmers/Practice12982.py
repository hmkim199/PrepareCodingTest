# https://programmers.co.kr/learn/courses/30/lessons/12982
# 예산

def solution(d, budget):
    answer = 0
    costs = sorted(d)
    total = 0
    for cost in costs:
        if total + cost <= budget:
            total += cost
            answer += 1
        else:
            break
    return answer
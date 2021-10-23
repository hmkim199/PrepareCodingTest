# https://programmers.co.kr/learn/courses/30/lessons/12912
# 두 정수 사이의 합


# 예전 코드
def solution(a, b):
    answer = 0
    if a == b:
        return a
    a, b = min(a, b), max(a, b)
    for emt in range(a, b+1):
        answer += emt
    return answer


# 지금 코드
def solution(a, b):
    answer = 0
    a, b = min(a, b), max(a, b)
    for i in range(a, b+1):
        answer += i
    return answer
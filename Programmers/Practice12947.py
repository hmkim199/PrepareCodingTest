# https://programmers.co.kr/learn/courses/30/lessons/12947
# 히샤드 수

# 1. 문자열 사용
def solution(x):
    answer = True
    sum = 0
    for s in str(x):
        sum += int(s)
    if x % sum != 0:
        answer = False
    return answer

# # 2. 나누기 이용
# def solution(x):
#     answer = True
#     temp = x
#     sum = 0
#     while temp > 0:
#         sum += temp % 10
#         temp //= 10
#     if x % sum != 0:
#         answer = False
#     return answer
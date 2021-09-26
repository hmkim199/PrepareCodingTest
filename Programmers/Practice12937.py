# https://programmers.co.kr/learn/courses/30/lessons/12937
# 짝수와 홀수

def solution(num):
    answer = ''
    if num % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer


# 다른 풀이
def solution(num):
    answer = 'Odd'
    if num % 2 == 0:
        answer = "Even"
    return answer
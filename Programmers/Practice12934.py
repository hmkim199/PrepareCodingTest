# https://programmers.co.kr/learn/courses/30/lessons/12934
# 정수 제곱근 판별

import math

def solution(n):
    answer = -1
    if math.sqrt(n) == int(math.sqrt(n)):
        answer = math.sqrt(n) + 1
        answer *= answer
    return answer


# 다른 풀이
import math

def solution(n):
    answer = -1
    x = math.sqrt(n)
    if x == int(x):
        answer = (x+1)**2
    return answer


# 다른 사람 풀이
def solution(n):
    answer = -1
    x = n ** (1/2)
    if x == int(x):
        answer = (x+1)**2
    return answer
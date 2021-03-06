# https://programmers.co.kr/learn/courses/30/lessons/77884
# 약수의 개수와 덧셈

# 내 풀이
import math

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0: 
            answer += i
        else: 
            answer -= i
    return answer


# 다른 사람 풀이
# 제곱수만 약수의 개수가 홀수개이다!!!!!

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
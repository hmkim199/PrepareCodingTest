# 약수의 합
# https://programmers.co.kr/learn/courses/30/lessons/12928

# 과거 풀이
# import math

# def solution(n):
#     answer = 0
#     for i in range(1, int(math.sqrt(n))+1):
#         j = n//i
#         if n % i == 0 and i != j:
#             answer += (i + j)
#         elif n % i == 0:
#             answer += i
#     return answer

import math

def solution(n):
    answer = 0
    
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            answer += i
            answer += (n//i)

            if n//i == i:
                answer -= i
    return answer
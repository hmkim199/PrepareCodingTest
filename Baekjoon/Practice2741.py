# 일리스 알고리즘 스터디 6주차
# #########################################
# 백준
# ######################################### 


# https://www.acmicpc.net/problem/2741
# N 찍기


N = int(input())
for i in range(N):
    print(i+1)


# https://www.acmicpc.net/problem/2742
# 기찍 N

N = int(input())
for i in range(N, 0, -1):
    print(i)


# https://www.acmicpc.net/problem/2753
# 윤년

year = int(input())
if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    print(1)
else:
    print(0)



# ###########################################
# 프로그래머스
# ###########################################


# https://programmers.co.kr/learn/courses/30/lessons/12934
# 정수 제곱근 판별

# 예전 풀이
def solution(n):
    answer = -1
    x = n ** (1/2)
    if x == int(x):
        answer = (x+1)**2
    return answer


# 현재 풀이
import math
def solution(n):
    answer = math.sqrt(n)
    return (answer+1) ** 2 if int(answer) == answer else -1



# https://programmers.co.kr/learn/courses/30/lessons/12933
# 정수 내림차순으로 배치하기

# 예전 풀이
def solution(n):
    answer = int(''.join(sorted(list(str(n)), reverse=True)))
    return answer

# 현재 풀이
def solution(n):
    answer = list(str(int(n)))
    answer.sort(reverse=True)
    return int("".join(answer))


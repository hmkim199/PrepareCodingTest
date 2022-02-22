# 일리스 알고리즘 스터디 5주차

# https://www.acmicpc.net/problem/2577
# 숫자의 개수

A = int(input())
B = int(input())
C = int(input())

mul = str(A*B*C)

for i in range(10):
    print(mul.count(str(i)))

# ==============================================
# https://www.acmicpc.net/problem/2675
# 문자열 반복

T = int(input())
for i in range(T):
    R, S = input().split()
    R = int(R)
    result = ""
    for c in S:
        result += c*R
    print(result)

# ================================================
# https://www.acmicpc.net/problem/2739
# 구구단

N = int(input())
for i in range(1, 10):
    print(str(N)+" * "+str(i)+" = "+str(N*i))

# =================================================
# https://programmers.co.kr/learn/courses/30/lessons/12937
# 짝수와 홀수

def solution(num):
    answer = 'Odd'
    if num % 2 == 0:
        answer = "Even"
    return answer

# =================================================
# https://programmers.co.kr/learn/courses/30/lessons/12935
# 제일 작은 수 제거하기

def solution(arr):
    answer = []
    i = arr.index(min(arr))
    answer = arr[:i]+arr[i+1:]
    return answer if len(answer) > 0 else [-1]
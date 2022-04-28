# https://www.acmicpc.net/problem/10998
# A×B

A, B = map(int, input().split())
print(A*B)


# https://www.acmicpc.net/problem/11654
# 아스키 코드

s = input()
print(ord(s))


# https://www.acmicpc.net/problem/11720
# 숫자의 합

N = int(input())
nums = map(int, list(input()))
print(sum(nums))


# https://programmers.co.kr/learn/courses/30/lessons/12917
# 문자열 내림차순으로 배치하기

def solution(s):
    return ''.join(sorted(s, reverse=True))


# https://programmers.co.kr/learn/courses/30/lessons/12916
# 문자열 내 p와 y의 개수

def solution(s):
    answer = True
    s = s.lower()
    if s.count("p") != s.count("y"):
        answer = False

    return answer
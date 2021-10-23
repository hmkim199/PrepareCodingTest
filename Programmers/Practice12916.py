# https://programmers.co.kr/learn/courses/30/lessons/12916
# 문자열 내 p와 y의 개수

def solution(s):
    answer = True
    s = s.lower()
    if s.count('p') != s.count('y'):
        answer = False
    return answer
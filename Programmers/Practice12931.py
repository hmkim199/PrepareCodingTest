# https://programmers.co.kr/learn/courses/30/lessons/12931
# 자릿수 더하기

def solution(n):
    answer = sum(list(map(int, str(n))))
    return answer
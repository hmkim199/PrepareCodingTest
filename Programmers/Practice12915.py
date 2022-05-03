# https://programmers.co.kr/learn/courses/30/lessons/12915
# 문자열 내 마음대로 정렬하기


# 예전 코드
def solution(strings, n):
    answer = strings
    answer.sort()
    answer.sort(key = lambda x : x[n], reverse = False)
    return answer


# 지금 코드
def solution(strings, n):
    answer = strings
    answer.sort()
    answer.sort(key=lambda x: x[n])
    return answer


# 풀이 3
def solution(strings, n):
    answer = sorted(strings, key=lambda x: (x[n], x))
    return answer
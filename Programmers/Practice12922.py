# https://programmers.co.kr/learn/courses/30/lessons/12922
# 수박수박수박수박수박수?


# 예전 코드
def solution(n):
    answer = ''
    first = '수'
    second = '박'
    for i in range(n):
        if i % 2 == 0:
            answer += first
        else:
            answer += second
    return answer


# 현재 코드
def solution(n):
    answer = '수박'*(n//2) + '수'*(n%2)
    return answer
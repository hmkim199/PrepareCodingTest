# https://programmers.co.kr/learn/courses/30/lessons/12917
# 문자열 내림차순으로 배치하기


# 예전 코드
def solution(s):
    return ''.join(sorted(s)[::-1])

# 지금 코드
def solution(s):
    return ''.join(sorted(s, reverse=True))
# https://programmers.co.kr/learn/courses/30/lessons/12918
# 문자열 다루기 기본

# 예전 코드
def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        answer = s.isdigit()
    return answer

# 지금 코드 -> 파이썬 삼항연산자 활용
def solution(s):
    answer = s.isdigit() if len(s) == 4 or len(s) == 6 else False

    return answer


# 타인 코드
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)
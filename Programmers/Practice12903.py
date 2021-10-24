# https://programmers.co.kr/learn/courses/30/lessons/12903
# 가운데 글자 가져오기


def solution(s):
    answer = ''
    middle = len(s)//2
    if len(s) % 2 == 0:
        answer += (s[middle-1] + s[middle])
    else:
        answer += s[middle]
    return answer



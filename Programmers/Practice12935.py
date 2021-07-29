# https://programmers.co.kr/learn/courses/30/lessons/12935
# 제일 작은 수 제거하기

def solution(arr):
    answer = arr
    answer.remove(min(answer))
    if len(answer) == 0:
        answer=[-1]
    return answer
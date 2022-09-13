# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# 짝지어 제거하기

from collections import deque

def solution(s):
    stack = deque()
    for c in s:
        if stack and c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    if stack:
        return 0
    return 1
    

    return answer
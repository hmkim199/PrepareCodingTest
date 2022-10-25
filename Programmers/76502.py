# https://school.programmers.co.kr/learn/courses/30/lessons/76502
# 괄호 회전하기

from collections import deque

def parenthesis(s):
    paren = {"[": "]", "(": ")", "{": "}"}
    stack = deque()
    for c in s:
        if c in paren:
            stack.append(c)
        elif stack:
            top = stack.pop()
            if paren[top] != c:
                return False
        else:
            return False
    if not stack:
        return True
    return False

def solution(s):
    answer = 0
    for i in range(len(s)):
        rot_s = s[i:] + s[:i]
        if parenthesis(rot_s):
            answer += 1
    return answer
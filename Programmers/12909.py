# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 올바른 괄호


from collections import deque

def solution(s):
    answer = True
    queue = deque()
    for c in s:
        if c == '(':
            queue.append(c)
        else:
            if not queue:
                answer = False
                break
            queue.pop()
    if queue:
        answer = False
    

    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/42587?language=python3
# 프린터

from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque()
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    
    order = 0
    while q:
        paper, idx = q.popleft()
        for p in q:
            if p[0] > paper:
                q.append((paper, idx))
                break
        else:
            order += 1
            if idx == location:
                return order
        
    return answer
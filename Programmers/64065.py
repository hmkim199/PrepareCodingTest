# https://school.programmers.co.kr/learn/courses/30/lessons/64065
# 튜플

def solution(s):
    s = s[2:-2].split("},{")
    answer = [set() for _ in range(len(s)+1)]
    for li in s:
        elems = set(li.split(","))
        answer[len(elems)] = elems
    
    for i in range(len(answer)-1, 0, -1):
        answer[i] = int((answer[i]-answer[i-1]).pop())
    return answer[1:]
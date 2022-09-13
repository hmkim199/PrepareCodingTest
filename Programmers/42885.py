# https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 구명보트

from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    people = deque(people)
    
    while people:
        maxi = people.popleft()
        answer += 1
        while people and maxi + people[-1] <= limit:
            maxi += people.pop()
        
    return answer
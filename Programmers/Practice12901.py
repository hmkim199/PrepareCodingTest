# https://programmers.co.kr/learn/courses/30/lessons/12901
# 2016년

# 예전 코드
def solution(a, b):
    week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    days = 0
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(a-1):
        days += month[i]
    days += b
    days = days % 7
    return week[days]


# 현재 코드
import datetime
def solution(a, b):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    answer = days[datetime.date(2016, a, b).weekday()]
    return answer
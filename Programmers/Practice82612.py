# https://programmers.co.kr/learn/courses/30/lessons/82612
# 부족한 금액 계산하기

def solution(price, money, count):
    answer = -1
    needMoney = 0
    for i in range(1, count+1):
        needMoney += price*i
    answer = needMoney - money
    if answer > 0:
        return answer
    else:
        answer = 0
    return answer
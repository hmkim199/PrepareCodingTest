# https://programmers.co.kr/learn/courses/30/lessons/12943
# 콜라츠 추측

def solution(num):
    answer = 0
    for i in range(500):
        if num == 1:
            return answer
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        answer += 1
    answer = -1
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/12911
# 다음 큰 숫자


def solution(n):
    found = False
    cnt1 = bin(n).count('1')
    temp = n+1
    while not found:
        temp_cnt = bin(temp).count('1')
        if temp_cnt == cnt1:
            break
        temp += 1
    
    return temp
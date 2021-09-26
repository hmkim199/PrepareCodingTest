# https://programmers.co.kr/learn/courses/30/lessons/12940
# 최대공약수와 최소공배수

def solution(n, m):
    answer = []
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    answer.append(answer[0] * (n // answer[0]) * (m // answer[0]))
    return answer


#다른 풀이 - 유클리드 호제법
def solution(n, m):
    answer = []
    a, b = max(n, m), min(n, m)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    answer.append(a)
    answer.append(n*m//a)
        
    return answer
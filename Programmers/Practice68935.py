# https://programmers.co.kr/learn/courses/30/lessons/68935
# 3진법 뒤집기

# 예전 코드
def solution(n):
    answer = ''
    result = 0
    while n >= 3: # 3일 경우를 생각하지 않아서 틀렸었음.
        answer += str(n % 3)
        n = n // 3
    answer += str(n)
    for i in range(len(answer)-1, -1, -1):
        result += int(answer[i]) * (3**(len(answer)-1-i))
    return result
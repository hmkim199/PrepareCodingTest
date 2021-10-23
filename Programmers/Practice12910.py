# https://programmers.co.kr/learn/courses/30/lessons/12910
# 나누어 떨어지는 숫자 배열


# 예전 코드
def solution(arr, divisor):
    answer = []
    for element in arr:
        if element % divisor == 0:
            answer.append(element)
    if answer == []:
        answer.append(-1)
    answer.sort()
    return answer


# 지금 코드
def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()
    
    return answer
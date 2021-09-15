# https://programmers.co.kr/learn/courses/30/lessons/12954
# x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = []
    
    for i in range(1, n+1):
        answer.append(x * i)
        #print(answer[i-1])
    
    return answer


# 다른 사람 풀이
# def number_generator(x, n):
#     
#     return [i * x + x for i in range(n)]
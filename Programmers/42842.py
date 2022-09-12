# https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 카펫

def solution(brown, yellow):
    x = int((brown+4) + ((brown+4)**2-16*(brown+yellow))**(1/2)) // 4
    y = int((brown+4) - ((brown+4)**2-16*(brown+yellow))**(1/2)) // 4
    return [x, y]

# 아래는 통과했지만 찝찝한코드..
# def solution(brown, yellow):
#     answer = [0, 0]
#     total = brown + yellow
#     end = 2500 if total//3+1 > 2500 else 2500
#     for i in range(3, end):
#         for j in range(i, end):
#             if i*j == total and 2*j + 2*i - 4 == brown:
#                 answer[0] = j
#                 answer[1] = i
#                 return answer
#     return answer
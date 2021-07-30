# https://programmers.co.kr/learn/courses/30/lessons/12932
# 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = list(map(int, str(n)))
    answer.reverse()
    return answer


# 타인 풀이
# def digit_reverse(n):
#     return list(map(int, reversed(str(n))))

# 과거 풀이
# def solution(n):
#     answer = list(map(int, str(n)[::-1]))
#     return answer
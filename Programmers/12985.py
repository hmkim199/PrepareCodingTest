# https://school.programmers.co.kr/learn/courses/30/lessons/12985
# 예상 대진표

# 시간 초과
# def next_number(num):
#     """
#     대결 후 다음 라운드에 가지는 숫자 리턴.
#     """
#     return (num+1) // 2

# def solution(n,a,b):
#     answer = 1
#     new_a = next_number(a)
#     new_b = next_number(b)
    
#     while True:
#         new_a, new_b = min(new_a, new_b), max(new_a, new_b)
#         if new_b % 2 == 0 and new_b - 1 == new_a:
#             return answer + 1
#         else:
#             new_a = next_number(new_a)
#             new_b = next_number(new_b)
#             answer += 1
#     return answer + 1


# 실패, 런타임 에러
# from math import log2

# def solution(n,a,b):
#     answer = 0
#     a, b = min(a, b), max(a, b)
#     if a % 2 == 1:
#         a += 1
#     if b % 2 == 1:
#         b += 1
    
#     answer = int(log2(b-a)) + 1

#     return answer

# 시간초과였던 처음 풀이에서 한끝 차이인 것 같은데 통과함. 역시 재귀호출이 시간 오래 걸리네..
def solution(n,a,b):
    answer = 0
    new_a, new_b = min(a, b), max(a, b)
    
    while True:
        if new_b % 2 == 0 and new_b - 1 == new_a:
            return answer + 1
        else:
            new_a = (new_a+1) // 2
            new_b = (new_b+1) // 2
            answer += 1
    return answer + 1

# 다른 사람 풀이. 내 아이디어랑 거의 비슷한데 좀 더 간결함.
def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer
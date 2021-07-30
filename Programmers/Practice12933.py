# https://programmers.co.kr/learn/courses/30/lessons/12933
# 정수 내림차순으로 배치하기

def solution(n):
    answer = 0
    temp = sorted(list(map(int, str(n))), reverse=True)
    answer = int("".join(map(str, temp)))
    return answer


# 타인 풀이
# def solution(n):
#     ls = list(str(n))
#     ls.sort(reverse = True)
#     return int("".join(ls))
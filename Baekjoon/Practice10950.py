# https://www.acmicpc.net/problem/10950
# A+B - 3


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(A+B)


# https://www.acmicpc.net/problem/10951
# A+B - 4

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break


# https://www.acmicpc.net/problem/10952
# A+B - 5

while True:
    A, B = map(int, input().split())
    if A+B == 0:
        break
    print(A+B)


# https://programmers.co.kr/learn/courses/30/lessons/12919
# 서울에서 김서방 찾기

def solution(seoul):
    answer = '김서방은 '+str(seoul.index("Kim"))+ '에 있다' 
    return answer


# https://programmers.co.kr/learn/courses/30/lessons/12918
# 문자열을 정수로 바꾸기 기본

# 저번 풀이
def solution(s):
    answer = s.isdigit() if len(s) == 4 or len(s) == 6 else False
    # if s.isdigit():
    #     if len(s) == 4 or len(s) == 6:
    #         answer = True
    return answer

# 이번 풀이
def solution(s):
    answer = False
    if len(s) in (4, 6) and s.isdigit():
        answer = True
    return answer
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
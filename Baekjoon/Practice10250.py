# https://www.acmicpc.net/problem/10250
# ACM 호텔


# T = int(input())
# for i in range(T):
#     H, W, N = map(int, input().split())
#     floor = N % H
#     num = N // H + 1
#     if N % H == 0:
#         floor = H
#         num = N // H
#     print(floor * 100 + num)


# 이번 풀이

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())

    floor = N%H
    number = str(1+N//H)

    if N % H == 0:
        floor = H
        number = str(N//H)
    
    if len(number) == 1:
        number = "0"+ number
        
    res = str(floor) + number
    print(res)

































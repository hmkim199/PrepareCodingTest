# https://www.acmicpc.net/problem/6064
# 카잉 달력

#  시간 초과
# T = int(input())
# for _ in range(T):
#     M, N, x, y = map(int, input().split())

#     temp_x = 1
#     temp_y = 1

#     year = 1
#     while temp_x != M or temp_y != N:
#         if temp_x == x and temp_y == y:
#             break

#         if temp_x < M:
#             temp_x += 1
#         elif temp_x == M:
#             temp_x = 1
        
#         if temp_y < N:
#             temp_y += 1
#         elif temp_y == N:
#             temp_y = 1
        
#         year += 1
#     else:
#         year = -1

#     print(year)

from math import gcd


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())

    smaller = min(x, y)
    temp_x = smaller
    temp_y = smaller
    gap = N
    if smaller == x:
        gap = M

    year = smaller
    end = M * N // gcd(M, N)

    answer = -1

    if temp_x == x and temp_y == y:
        answer = year
    else:
        while year <= end:
            year += gap
            temp_x = year % M
            temp_y = year % N

            if temp_x == 0:
                temp_x = M
            if temp_y == 0:
                temp_y = N

            if temp_x != x or temp_y != y:
                continue
            else:
                answer = year
                break
    print(answer)
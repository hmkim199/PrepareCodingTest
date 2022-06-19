# https://www.acmicpc.net/problem/9375
# 패션왕 신해빈

# 검색해서 품. 의상의 종류에 그 의상을 입지 않은 경우의 수를 더해서 모두 곱해주고 모두 안 입은 경우의 수 1을 빼준다.
T = int(input())
for _ in range(T):
    n = int(input())
    closet = {}
    for _ in range(n):
        name, t = input().split()
        if not closet.get(t):
            closet[t] = 1
        else:
            closet[t] += 1

    cnt = []
    count = 1
    for k in closet:
        count *= (closet[k]+1)
    print(count - 1)


# 메모리 초과
# from itertools import combinations

# def add_closet():
#     n = int(input())
#     closet = {}
#     for _ in range(n):
#         name, t = input().split()
#         if not closet.get(t):
#             closet[t] = 1
#         else:
#             closet[t] += 1

#     cnt = []
#     for k in closet:
#         cnt.append(closet[k])
#     return cnt


# T = int(input())
# for _ in range(T): 
#     cnt = add_closet()
#     count = 0
#     for i in range(1, len(cnt)+1):   
#         combi = list(combinations(cnt, i))
#         for c in combi:
#             temp = c[0]
#             for j in range(1, len(c)):
#                 temp *= c[j]
#             count += temp

#     print(count)
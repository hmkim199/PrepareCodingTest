# https://www.acmicpc.net/problem/11723
# 집합

# python, pypy 둘 다 런타임 에러
# import sys

# M = int(input())
# S = set()

# for _ in range(M):
#     operation = sys.stdin.readline().strip().split()
#     op = operation[0]
#     x = 0
#     if len(operation) > 1:
#         x = int(operation[1])

#     if op == 'add':
#         S.add(x)
#     elif op == 'remove':
#         S.remove(x)
#     elif op == 'check':
#         if x in S:
#             print(1)
#         else:
#             print(0)
#     elif op == 'toggle':
#         if x in S:
#             S.remove(x)
#         else:
#             S.add(x)
#     elif op == 'all':
#         S = {i for i in range(1, 21)}
#     elif op == 'empty':
#         S = set()


import sys

M = int(input())
S = [False for i in range(21)]

for _ in range(M):
    operation = sys.stdin.readline().strip().split()
    op = operation[0]
    x = 0
    if len(operation) > 1:
        x = int(operation[1])

    if op == 'add':
        S[x] = True
    elif op == 'remove':
        S[x] = False
    elif op == 'check':
        if S[x]:
            print(1)
        else:
            print(0)
    elif op == 'toggle':
        if S[x]:
            S[x] = False
        else:
            S[x] = True
    elif op == 'all':
        S = [True for i in range(21)]
    elif op == 'empty':
        S = [False for i in range(21)]
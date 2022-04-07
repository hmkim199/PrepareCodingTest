# https://www.acmicpc.net/problem/10818
# 최소, 최대

# N = int(input())
# nums = list(map(int, input().split()))

# print(min(nums), max(nums))


# https://www.acmicpc.net/problem/10869
# 사칙연산 

# A, B = map(int, input().split())

# print(A+B)
# print(A-B)
# print(A*B)
# print(A//B)
# print(A%B)


# https://www.acmicpc.net/problem/10871
# X보다 작은 수

N, X = map(int, input().split())
A = list(map(int, input().split()))

for num in A:
    if num < X:
        print(num, end=" ")
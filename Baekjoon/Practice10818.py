# https://www.acmicpc.net/problem/10818
# 최소, 최대

N = int(input())
nums = list(map(int, input().split()))

print(min(nums), max(nums))


# https://www.acmicpc.net/problem/10869
# 사칙연산 

A, B = map(int, input().split())

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)


# https://www.acmicpc.net/problem/10871
# X보다 작은 수

N, X = map(int, input().split())
A = list(map(int, input().split()))

for num in A:
    if num < X:
        print(num, end=" ")


# https://programmers.co.kr/learn/courses/30/lessons/12922
# 수박수박수박수박수박수?

# 예전 풀이
def solution(n):
    answer = '수박'*(n//2) + '수'*(n%2)
    return answer

# 이번 풀이
def solution(n):
    answer = '수박'*(n//2)
    return answer if n%2 == 0 else answer+'수'
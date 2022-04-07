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


# https://programmers.co.kr/learn/courses/30/lessons/12921
# 소수 찾기

# 예전 풀이
def solution(n):
    answer = 0
    isPrime = [True for _ in range(n+1)]
    isPrime[0], isPrime[1] = False, False
    
    for i in range(len(isPrime)):
        if isPrime[i] == True:
            answer += 1
            for j in range(2, len(isPrime)):
                if i*j > len(isPrime)-1:
                    break
                isPrime[i*j] = False

    
    return answer

# 이번 풀이
# 단순 2중 for문 돌면 시간 초과
def solution(n):
    answer = 0
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = is_prime[1] = False
    for i in range(2, n+1):
        if is_prime[i] == True:
            answer += 1
            for j in range(2, n//i+1):
                is_prime[i*j] = False

    return answer
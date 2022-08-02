# https://www.acmicpc.net/problem/1389
# 케빈 베이컨의 6단계 법칙

from collections import deque

N, M = map(int, input().split())
friends = [
    set() for _ in range(N+1)
]

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].add(b)
    friends[b].add(a)

for i in range(N+1):
    friends[i] = sorted(friends[i])

def bfs(i, j):
    """ i부터 j까지의 최단 경로(거리) 반환"""
    if i == j:
        return 0
    visited = [False for _ in range(N+1)]
    queue = deque([i])
    visited[i] = True
    predecessor = [None for _ in range(N+1)]
    while queue:
        user = queue.popleft()
        for friend in friends[user]:
            if not visited[friend]:
                visited[friend] = True
                queue.append(friend)
                predecessor[friend] = user

    distance = 0
    temp = j
    while temp:
        distance += 1
        temp = predecessor[temp]  # temp를 다음 노드로 바꿔준다
    return distance-1


kevin_nums = [0 for _ in range(N+1)]
# 1~N까지의 각각의 케빈 베이컨 수 구하기
for i in range(1, N+1):
    for j in range(1, N+1):
        kevin_nums[i] += bfs(i, j)

print(kevin_nums.index(min(kevin_nums[1:])))


# https://www.acmicpc.net/problem/1463
# 1로 만들기

count = [0] * 1000001
count[2] = count[3] = 1

for i in range(4, 1000001):
    temp = []
    if i%3 == 0:
        temp.append(count[i//3] + 1)
    if i%2 == 0:
        temp.append(count[i//2] + 1)
    
    temp.append(count[i-1] + 1)
    count[i] = min(temp)

N = int(input())

print(count[N])


# https://www.acmicpc.net/problem/1541
# 잃어버린 괄호

equation = input().split("-")
result = 0
for i in range(len(equation)):
    temp = sum(map(int, equation[i].split("+")))
    if i == 0:
        result += temp
    else:
        result -= temp

print(result)


# https://www.acmicpc.net/problem/1620
# 나는야 포켓몬 마스터 이다솜

import sys

N, M = map(int, sys.stdin.readline().strip().split())

poketmon = {}
for i in range(N):
    p = sys.stdin.readline().strip()
    poketmon[p] = i+1
    poketmon[str(i+1)] = p

ans = []
for _ in range(M):
    ans.append(poketmon[sys.stdin.readline().strip()])
    # print(poketmon[input()])

print(*ans, sep='\n')

# # https://school.programmers.co.kr/learn/courses/30/lessons/12924
# # 숫자의 표현

def solution(n):
    answer = 0
    for i in range(1, n+1):
        temp = 0
        for j in range(i, n+1):
            temp += j
            if temp == n:
                answer += 1
                break
            elif temp > n:
                break
            
            
    return answer


# # https://school.programmers.co.kr/learn/courses/30/lessons/12923
# # 숫자 블록

# # 시간 초과
# def solution(begin, end):
#     answer = [0 for _ in range(end - begin + 1)]
#     for i in range(end//2, 0, -1):
#         for j in range(i*2, end+1, i):
#             if j-begin >= 0 and answer[j-begin] == 0:
#                 answer[j-begin] = i
#     return answer


# # 시간 초과
# def solution(begin, end):
#     answer = [0 for _ in range(end - begin + 1)]
#     end_block = 10000000 if end//2 > 10000000 else end//2
#     for i in range(end//2, 0, -1):
#         for j in range(i*2, end+1, i):
#             if j-begin >= 0 and answer[j-begin] == 0:
#                 answer[j-begin] = i
#     return answer

# # 시간 초과
# def solution(begin, end):
#     answer = [0 for _ in range(end - begin + 1)]
#     end_block = 10000000 if end//2 > 10000000 else end//2
#     for i in range(end_block, 0, -1):
#         for j in range(end, begin-1, -1):
#             if j < i*2:
#                 break
#             if j % i == 0:
#                 if answer[j-begin] == 0:
#                     answer[j-begin] = i

#     return answer

# # 실패
# def solution(begin, end):
#     answer = [0 for _ in range(end - begin + 1)]
#     end_block = 10**7 if end//2 > 10**7 else end//2
#     for i in range(end_block, 0, -1):
#         for j in range(end//i * i, begin-1, -i):
#             if j < i*2:
#                 break
#             if j % i == 0:
#                 if answer[j-begin] == 0:
#                     answer[j-begin] = i

#     return answer

# # 남의 풀이
# import math
# def solution(begin, end):
#     result = []
#     for i in range(begin, end+1):
#         # 1은 문제 조건상 0이므로, 0을 넣어준다.
#         if i < 2:
#             result.append(0)
#             continue
#         # 소수 판별하기.
#         for j in range(2, int(math.sqrt(i))+1):
#             # 소수가 아니면, 나눈 몫을 넣어준다
#             if i % j == 0 and i // j < 10**7:
#                 result.append(i // j)
#                 break
#         else:
#             result.append(1)
        
#     return result

# # 남의 풀이 보고 푼 내풀이
def solution(begin, end):
    answer = []
    end_block = 10**7
    for i in range(begin, end+1):
        if i < 2:
            answer.append(0)
            continue
        temp = 1
        for j in range(2, int(i**0.5)+1):
            if i%j == 0 and i//j <= end_block:
                temp = i//j
                break
        answer.append(temp)
        
    return answer


# https://school.programmers.co.kr/learn/courses/30/lessons/92335
# k진수에서 소수 개수 구하기

def convert(n, k):
    if k == 10:
        return str(n)
    d = n
    ans = ''
    while d > 0:
        ans = str(d%k) + ans
        d //= k
    return ans

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    k_num = convert(n, k)
    for i in range(len(k_num)):
        for j in range(i, len(k_num)):
            if '0' not in k_num[i:j+1] and is_prime(int(k_num[i:j+1])):
                
                if i > 0 and j < len(k_num)-2:
                    if k_num[i-1] == '0' and k_num[j+1] == '0':
                        answer += 1
                if i == 0 and j < len(k_num)-2:
                    if k_num[j+1] == '0':
                        answer += 1
                if i > 0 and j == len(k_num)-1:
                    if k_num[i-1] == '0':
                        answer += 1
                if i == 0 and j == len(k_num)-1:
                    answer += 1
    return answer

print(solution(437674, 3)) # 3
print(solution(110011, 10)) # 2

# https://school.programmers.co.kr/learn/courses/30/lessons/12914
# 멀리 뛰기

# 몇개 런타임 에러인데 아마 그냥 시간 초과인 듯.
# def jump(n, memo):
#     if n in memo:
#         return memo[n]
#     memo[n] = jump(n-1, memo) + jump(n-2, memo)
#     return memo[n]

# def solution(n):
#     memo = {1: 1, 2: 2}

#     return jump(n, memo) % 1234567

# print(solution(4))

# 풀이
def solution(n):
    jump = [0 for _ in range(2001)]
    jump[1] = 1
    jump[2] = 2
    for i in range(3, len(jump)):
        jump[i] = jump[i-2] + jump[i-1]

    return jump[n] % 1234567

print(solution(4))
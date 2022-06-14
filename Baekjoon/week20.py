# https://www.acmicpc.net/problem/7568
# 덩치 

N = int(input())
people = []
for _ in range(N):
    w, h = map(int, input().split())
    people.append((w, h))

rank = [1] * len(people)
for i in range(len(people)):
    for person in people[:i]+people[i+1:]:
        if people[i][0] < person[0] and people[i][1] < person[1]:
            rank[i] += 1

print(*rank, sep=" ")

# https://www.acmicpc.net/problem/9012
# 괄호 

T = int(input())
result = []
for _ in range(T):
    string = input()
    paren_stack = []
    right = True
    for c in string:
        if c == "(":
            paren_stack.append(c)
        else:
            try:
                paren_stack.pop()
            except:
                right = False

    if len(paren_stack) == 0 and right:
        result.append("YES")
    else:
        result.append("NO")

print(*result, sep="\n")

# https://www.acmicpc.net/problem/10250
# ACM 호텔

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

# https://www.acmicpc.net/problem/10773
# 제로 

import sys

K = int(input())

nums = []
for _ in range(K):
    i = int(sys.stdin.readline().strip())
    if i == 0:
        nums.pop()
    else:
        nums.append(i)

print(sum(nums))

# https://www.acmicpc.net/problem/10814
# 나이순 정렬

N = int(input())
members = []

for _ in range(N):
    members.append(input().split())

members.sort(key=lambda x: int(x[0]))

for li in members:
    print(*li)

# https://programmers.co.kr/learn/courses/30/lessons/12977
# 소수 만들기

def solution(nums):
    answer = 0
    length = len(nums)
    options = [] 
    for i in range(length):
        for j in range(i+1, length):
            for k in range(j+1, length):
                options.append(nums[i] + nums[j] + nums[k])

    maximum = max(options)
    is_prime = [True for i in range(maximum+1)]
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, maximum+1):
        if is_prime[i]:
            for j in range(i+i, maximum+1, i):
                is_prime[j] = False
                
    for op in options:
        if is_prime[op]:
            answer += 1
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/70128
# 내적

def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/76501
# 음양 더하기

def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if not signs[i]:
            absolutes[i] *= -1
    return sum(absolutes)

# https://programmers.co.kr/learn/courses/30/lessons/86051
# 없는 숫자 더하기

def solution(numbers):
    answer = 0
    numbers = set(numbers)
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/64061
# 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    basket = []
    j = 1
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                basket.append(board[i][move-1])
                board[i][move-1] = 0
                break
    # print(basket)
    while len(basket) > j:
        if basket[j-1] == basket[j]:
            answer += 2
            del basket[j]
            del basket[j-1]
            j = 1
            # print(basket)
            continue
        j += 1
            
    return answer
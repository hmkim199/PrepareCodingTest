# 벌집

N = int(input())
room = 1
count = 1
shape = 6
while room < N:
    if room + shape * count <= N:
        room += shape * count
    else:
        room = N
    count += 1

print(count)


# 최대공약수와 최소공배수
a, b = map(int, input().split())
a, b = max(a, b), min(a, b)

def gcd(a, b):
    while True:
        r = a % b
        if r == 0:
            break
        a = b
        b = r
    return b

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b)) 


# https://www.acmicpc.net/problem/2751
# 수 정렬하기 2

import sys

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline()))

nums.sort()
print(*nums, sep="\n")


# https://www.acmicpc.net/problem/2775
# 부녀회장이 될테야
 

T = int(input())
p = {}
def get_people(k, n):
    if k == 0:
        p[(k,n)] = n
        return n
    elif (k,n) in p:
        return p[(k,n)]
    else:
        people = 0
        for i in range(1, n+1):
            people += get_people(k-1, i)
        p[(k,n)] = people
        return people
    

for _ in range(T):
    k = int(input())
    n = int(input())
    print(get_people(k, n))


# https://www.acmicpc.net/problem/2798
# 블랙잭

N, M = map(int, input().split())
cards = list(map(int, input().split()))

total = 0
length = len(cards)
for i in range(length-2):
    for j in range(i+1, length-1):
        for k in range(j+1, length):
            temp = cards[i] + cards[j] + cards[k]
            if total < temp <= M:
                total = temp

print(total)


# 두 개 뽑아서 더하기
def solution(numbers):
    answer = []

    for i in range(0, len(numbers)):
        for j in numbers[i+1:]:
            answer.append(numbers[i]+j)
    answer = sorted(list(set(answer)))
    return answer



# 예산
def solution(d, budget):
    answer = 0
    costs = sorted(d)
    total = 0
    for cost in costs:
        if total + cost <= budget:
            total += cost
            answer += 1
        else:
            break
    return answer


# 3진법 뒤집기
def solution(n):
    answer = ""
    base = 3
    q = n
    while q != 0:
        answer += str(q % base)
        q = q // base
    
    return int(answer, base)



# 약수의 개수와 덧셈
import math

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0: 
            answer += i
        else: 
            answer -= i
    return answer


# 실패율
def solution(N, stages):
    answer = []
    stages.sort()

    for stage in range(1, N+1):
        fail = 0
        idx = -1
        for i in range(len(stages)):
            if stages[i] == stage:
                if fail == 0:
                    idx = i
                fail += 1
            elif stages[i] > stage:
                break
        answer.append([stage, fail/(len(stages)-idx)])
    
    answer.sort(key=lambda x:x[1], reverse=True)
    answer = [i[0] for i in answer]        
    return answer
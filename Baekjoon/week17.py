# https://www.acmicpc.net/problem/1966
# 프린터 큐

from collections import deque

testcases = int(input())
result = []
for _ in range(testcases):
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    indexed_importance = deque()
    count = 0
    for i in range(len(importance)):
        l = [i, importance[i]]
        indexed_importance.append(l)
    while True:
        priority = max(indexed_importance, key=lambda x: x[1])[1]
        if indexed_importance[0][1] == priority:
            p = indexed_importance.popleft()
            count += 1
            if p[0] == M:
                result.append(count)
                break
        else:
            indexed_importance.append(indexed_importance.popleft())

print(*result, sep="\n")


# https://www.acmicpc.net/problem/1978
# 소수 찾기

N = int(input())
nums = sorted(list(map(int, input().split())))
primes = [False, False] + [True]*(nums[-1]-1)

def prime(n):
    for i in range(2, n+1):
        if primes[i]:
            for j in range(2*i, n+1, i):
                primes[j] = False
            
def countPrime(primes, nums):
    count = 0
    for num in nums:
        if primes[num]:
            count += 1
    return count

prime(nums[-1])
print(countPrime(primes, nums))


# https://www.acmicpc.net/problem/2108
# 통계학
import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline().strip()))

nums.sort()
def average(nums):
    return round(sum(nums)/len(nums))

def center(nums):
    return nums[len(nums)//2]

def freq(nums):
    count = Counter(nums).most_common(2)
    if len(count)>1:
        if count[1][1] == count[0][1]:
            return count[1][0]
    return count[0][0]

def between(nums):
    return nums[-1]-nums[0]

print(average(nums))
print(center(nums))
print(freq(nums))
print(between(nums))


# https://www.acmicpc.net/problem/2164
# 카드2
N = int(input())
nums = [i+1 for i in range(N)]
idx = 0

while len(nums) - idx > 1:
    idx += 1
    nums.append(nums[idx])
    idx += 1

print(nums[idx])


# https://www.acmicpc.net/problem/2231
# 분해합
N = int(input())
creator = 0
for i in range(1, N):
    li = [i] + list(str(i))
    li = [int(i) for i in li]
    if sum(li) == N:
        creator = li[0]
        break
print(creator)

# https://programmers.co.kr/learn/courses/30/lessons/17681
# [1차] 비밀지도

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        originNum = bin(arr1[i] | arr2[i])[2:]
        originNum = '0' * (n-len(originNum)) + originNum
        mark = ''
        for j in originNum:
            if j == '1':
                mark += "#"
            else:
                mark += " "
        answer.append(mark)
    return answer

# https://programmers.co.kr/learn/courses/30/lessons/82612
# 부족한 금액 계산하기
def solution(price, money, count):
    answer = -1
    needMoney = 0
    for i in range(1, count+1):
        needMoney += price*i
    answer = needMoney - money
    if answer > 0:
        return answer
    else:
        answer = 0
    return answer


# https://programmers.co.kr/learn/courses/30/lessons/87389
# 나머지가 1이 되는 수 찾기
def solution(n):
    for x in range(2, n):
        if n % x == 1:
            return x


# https://programmers.co.kr/learn/courses/30/lessons/86491
# 최소직사각형
def solution(sizes):
    w, h = 0, 0

    for l, r in sizes:
        l, r = max(l, r), min(l, r)
        w = max(w, l)
        h = max(h, r)
        
    return w * h

# https://programmers.co.kr/learn/courses/30/lessons/12901
# 2016년
import datetime
def solution(a, b):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    answer = days[datetime.date(2016, a, b).weekday()]
    return answer
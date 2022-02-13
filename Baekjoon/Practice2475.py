# 일리스 알고리즘 스터디 4주차

# https://www.acmicpc.net/problem/2475
# 검증수

# nums = list(map(int, input().split()))
# nums = [x**2 for x in nums]
# print(sum(nums)%10)

# ===============================================
# https://www.acmicpc.net/problem/2557
# Hello World

# print("Hello World!")

# ===============================================
# https://www.acmicpc.net/problem/2562
# 최댓값

# 예전 풀이
nums = []
for i in range(9):
    nums.append(int(input()))
    
maximum = max(nums)

print(maximum)
print(nums.index(maximum)+1)

# 이번 풀이
I = 9
d = {}
for i in range(I):
    d[i+1] = int(input())
print(max(d.values()))
print(max(d, key=d.get))
# print(max(d.keys(), key=lambda k: d[k]))


# ================================================
# https://programmers.co.kr/learn/courses/30/lessons/12943
# 콜라츠 추측

# 예전 풀이
def solution(num):
    answer = -1
    for i in range(500):
        if num == 1:
            return i
        elif num%2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
    return answer

# 이번 풀이
def solution(num):
    answer = 0
    while answer < 500 and num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num*3+1
        answer += 1
    return answer if answer<500 else -1


# =================================================
# https://programmers.co.kr/learn/courses/30/lessons/12940
# 최대공약수와 최소공배수

# 예전 풀이
def solution(n, m):
    answer = []
    a, b = max(n, m), min(n, m)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    answer.append(a)
    answer.append(n*m//a)
        
    return answer


# 지금 풀이
def gcd(n, m):
    # 유클리드 호제법 : a / b = x ... r 나머지가 0일 때의 b 가 최대 공약수
    while n % m != 0:
        r = n % m
        n = m
        m = r
    return m
    
def lcm(n, m, g):
    return n * m // g

def solution(n, m):
    answer = []
    n, m = max(n, m), min(n, m)
    g = gcd(n, m)
    answer.append(g)
    answer.append(lcm(n, m, g))
    return answer
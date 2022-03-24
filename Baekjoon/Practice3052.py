# https://www.acmicpc.net/problem/3052
# 나머지 

nums = []

for _ in range(10):
    num = int(input())
    nums.append(num%42)

print(len(set(nums)))


# https://www.acmicpc.net/problem/8958
# OX퀴즈

T = int(input())

for _ in range(T):
    testcase = input()
    answer = [0 for i in range(len(testcase))]
    for i in range(len(testcase)):
        if testcase[i] == "O":
            answer[i] += 1
            if i != 0:
                answer[i] += answer[i-1]
    print(sum(answer))


# https://www.acmicpc.net/problem/9498
# 시험 성적 

num = int(input())
if 90 <= num <= 100:
    print("A")
elif 80 <= num < 90:
    print("B")
elif 70 <= num < 80:
    print("C")
elif 60 <= num < 70:
    print("D")
else:
    print("F")



# https://programmers.co.kr/learn/courses/30/lessons/12930
# 이상한 문자 만들기

# 예전 풀이
def solution(s):
        return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

# 이번 풀이
def solution(s):
    answer = ""
    idx = 0
    for c in s:
        if c.isalpha():
            if idx%2 == 0:
                answer += c.upper()
            else:
                answer += c.lower()
            idx += 1
        else:
            idx = 0
            answer += c
    
    return answer


# https://programmers.co.kr/learn/courses/30/lessons/12928
# 약수의 합

# 예전 풀이
import math

def solution(n):
    answer = 0
    
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            answer += i
            answer += (n//i)

            if n//i == i:
                answer -= i
    return answer


# 이번 풀이
def solution(n):
    answer = 0
    for i in range(1, int(n**(1/2)+1)):
        if n % i == 0:
            answer += i
            if n//i != i:
                answer += n//i
    return answer
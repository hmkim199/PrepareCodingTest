# 일리스 알고리즘 스터디 3주차

# https://www.acmicpc.net/problem/1546
# 평균

N = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)
for i in range(len(scores)):
    scores[i] = scores[i]/max_score * 100

print(sum(scores)/len(scores))

# =========================================
# https://www.acmicpc.net/problem/2438
# 별 찍기 - 1

N = int(input())
for i in range(N):
    print("*"*(i+1))

# ==========================================
# https://www.acmicpc.net/problem/2439
# 별 찍기 - 2

N = int(input())
for i in range(1, N+1):
    print(" " * (N-i) + "*" * i)

# ==========================================
# https://programmers.co.kr/learn/courses/30/lessons/12947
# 하샤드 수

# 풀이 1
def solution(x):
    answer = True
    sum = 0
    for i in str(x):
        sum += int(i)
    if x % sum != 0:
        answer = False
    return answer

# 풀이 2
def solution(x):
    li_x = [int(i) for i in list(str(x))]
    return x % sum(li_x) == 0

# ===========================================
# https://programmers.co.kr/learn/courses/30/lessons/12944
# 평균 구하기

def solution(arr):
    return sum(arr)/len(arr)
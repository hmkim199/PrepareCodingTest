# https://www.acmicpc.net/problem/2805
# 나무 자르기 

N, M = map(int, input().split())
heights = list(map(int, input().split()))

start = 0
end = max(heights)
mid = 0

while start <= end:
    mid = (start+end) // 2
    remain = 0
    for h in heights:
        if h > mid:
            remain += h-mid
    if remain < M:
        end = mid - 1
    elif remain > M:
        start = mid + 1
    else:
        break

print((start+end) // 2)

# =======================================================

# https://www.acmicpc.net/problem/2839
# 설탕 배달



N = int(input())

bags = (3, 5)
count = [N%bags[1]//bags[0], N // bags[1]]
possible = True

def sum_sugar():
    total = 0
    for i in range(len(bags)):
        total += bags[i]*count[i]
    return total

while sum_sugar() != N:
    count[1] -= 1
    count[0] = (N - bags[1]*count[1])//bags[0]
    
    if count[1] < 0:
        possible = False
        break

if not possible:
    print(-1)
else:
    print(sum(count))

# =======================================================
# https://www.acmicpc.net/problem/2869
# 달팽이는 올라가고 싶다
import math

A, B, V = map(int, input().split()) # 낮에 A미터 올라가고 밤에 B미터 미끄러지고 V만큼 나무 올라야 함.
# Ax-B(x-1)>V   =>  x > (V-B)/(A-B)

day = math.ceil((V-B)/(A-B))
print(day)

# =======================================================
# https://www.acmicpc.net/problem/4153
# 직각삼각형
res=[]
while True:
    t = sorted(list(map(int, input().split())))
    if sum(t) == 0:
        break
    elif t[0]**2 + t[1]**2 == t[2]**2:
        res.append("right")
    else:
        res.append("wrong")

print(*res, sep="\n")

# =======================================================
# https://www.acmicpc.net/problem/4949
# 균형잡힌 세상
from collections import deque

paren = {"(":")", "[":"]"}
res = []

while True:
    sentence = input()
    if sentence == ".":
        break

    paren_stack = deque()
    right = True
    for c in sentence:
        if c in ("(", "["):
            paren_stack.append(c)
        elif c in(")", "]"):
            try:
                temp = paren_stack.pop()
                if paren[temp] != c:
                    right = False
                    break
            except:
                right = False
                break
    
    if len(paren_stack) == 0 and right:
        res.append("yes")
    else:
        res.append("no")

print(*res, sep="\n")

# =======================================================

# https://programmers.co.kr/learn/courses/30/lessons/1845?language=python3
# 폰켓몬

def solution(nums):
    cnt = len(nums)//2
    ponketmon = {}
    for num in nums:
        if ponketmon.get(num):
            ponketmon[num] += 1
        else:
            ponketmon[num] = 1
    if len(ponketmon) > cnt:
        return cnt
    else:
        return len(ponketmon)


# =======================================================

# https://programmers.co.kr/learn/courses/30/lessons/42862
# 체육복
def solution(n, lost, reserve):
    reserve_only = set(reserve) - set(lost)
    lost_only = set(lost) - set(reserve)
    
    for r in reserve_only:
        if r-1 in lost_only:
            lost_only.remove(r-1)
        elif r+1 in lost_only:
            lost_only.remove(r+1)

    return n - len(lost_only)

# =======================================================

# https://programmers.co.kr/learn/courses/30/lessons/42840
# 모의고사
def solution(answers):
    answer = []
    result = {1: 0, 2: 0, 3: 0}
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    while len(first) <= len(answers):
        first += first
    while len(second) <= len(answers):
        second += second
    while len(third) <= len(answers):
        third += third
    
    for i in range(len(answers)):
        if first[i] == answers[i]:
            result[1] += 1
        if second[i] == answers[i]:
            result[2] += 1
        if third[i] == answers[i]:
            result[3] += 1
    
    highest = max(result.values())
    answer = [k for k,v in result.items() if highest == v]

    return answer
# =======================================================

# https://programmers.co.kr/learn/courses/30/lessons/42748
# k번째수
def solution(array, commands):
    answer = []
    for idx in range(len(commands)):
        i = commands[idx][0]-1
        j = commands[idx][1]
        k = commands[idx][2]-1
        answer.append(sorted(array[i:j])[k])
    return answer

# =======================================================

# https://programmers.co.kr/learn/courses/30/lessons/42576
# 완주하지 못한 선수

from collections import Counter

def solution(participant, completion):
    return list((Counter(participant)-Counter(completion)).keys())[0]
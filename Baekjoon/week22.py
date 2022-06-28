# https://www.acmicpc.net/problem/11650
# 좌표 정렬하기 

N = int(input())

points = []
for _ in range(N):
    point = list(map(int, input().split()))
    points.append(point)

points.sort(key=lambda x: (x[0], x[1]))

for p in points:
    print(*p)


# https://www.acmicpc.net/problem/11651
# 좌표 정렬하기 2

N = int(input())
points = []

for _ in range(N):
    point = list(map(int, input().split()))
    points.append(point)

points.sort(key=lambda x: (x[1], x[0]))

for p in points:
    print(*p)


# https://www.acmicpc.net/problem/11866
# 요세푸스 문제 0

N, K = map(int, input().split())

people = [i+1 for i in range(N)]
idx = 0
order = []
while people:
    idx = (idx+K-1)%len(people)
    order.append(people.pop(idx))

print("<", end="")
print(", ".join(map(str, order)), end="")
print(">")


# https://www.acmicpc.net/problem/15829
# Hashing 

L = int(input())
s = list(input())
M = 1234567891

# 아스키코드 97 == a
for i in range(len(s)):
    s[i] = (ord(s[i])-96)*31**i

print(sum(s)%M)


# https://www.acmicpc.net/problem/18111
# 마인크래프트 

# pypy
import sys

N, M, B = map(int, sys.stdin.readline().split())

# 블록제거 2초, 쌓기 1초
ground = []
for _ in range(N):
    ground.append(list(map(int, sys.stdin.readline().split())))

min_time, min_height = 10e9, 0
for height in range(257):
    bottom = top = 0
    for i in range(N):
        for j in range(M):
            if ground[i][j] < height:
                bottom += height-ground[i][j]
            else:
                top += ground[i][j]-height
    if bottom > top + B:
        continue
    time = bottom + top*2
    if time <= min_time:
        min_time = time
        min_height = height
print(min_time, min_height)


# https://www.acmicpc.net/problem/1003
# 피보나치 함수

fibo = []

for i in range(41):
    if i == 0:
        fibo.append((1, 0))
    elif i == 1:
        fibo.append((0, 1))
    else:
        fibo.append((fibo[i-1][0]+fibo[i-2][0], fibo[i-1][1]+fibo[i-2][1]))


T = int(input())
for i in range(T):
    N = int(input())
    print(*fibo[N])


# https://programmers.co.kr/learn/courses/30/lessons/12953#
# N개의 최소공배수

# 처음엔 for문 돌면서 gcd 값으로 계속 gcd 구했는데 틀림! lcm으로 gcd 갱신해야함.

def get_gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def solution(arr):
    lcm = arr[0]
    for i in range(1, len(arr)):
        temp = lcm
        gcd = get_gcd(lcm, arr[i])
        lcm = temp * arr[i] // gcd
    return lcm


# https://programmers.co.kr/learn/courses/30/lessons/12952
# N-Queen

def possible(x, y, n, col):
    for i in range(x):
        # 같은 열에 위치하는지 or 같은 대각선에 위치하는지 확인
        if y == col[i] or abs(y - col[i]) == x - i:
            return False
    return True

def queen(x, n, col):
    
    # row가 끝까지 갔으면 성공!
    if x == n:
        return 1
    
    count = 0
    
    for y in range(n):
        # 다음 퀸을 놓을 수 있는 경우만 진행
        if possible(x, y, n, col):
            col[x] = y # x번째 row의 col index 저장 ex) col[0] = 2 0번째 행의 2번째 col에 놓여져 있다.
            count += queen(x+1, n, col) # row index 증가 후 호출
            
    return count

def solution(n):
    
    col = [0] * n

    # 0은 세로축의 시작점 
    # n은 맵의 크기
    # col은 row 의 index를 담기 위한 리스트
    answer = queen(0, n, col)
    
    return answer


# https://programmers.co.kr/learn/courses/30/lessons/12951
# JadenCase 문자열 만들기

def solution(s):
    answer = ''
    is_first = True
    for i in range(len(s)):
        temp = s[i]
        if is_first:
            if s[i].isalpha():
                temp = s[i].upper()
            is_first = False
        else:
            if s[i].isalpha():
                temp = s[i].lower()
            elif s[i] == ' ' and i < len(s)-1 and s[i+1] != ' ':
                is_first = True
        answer += temp
    return answer


# https://programmers.co.kr/learn/courses/30/lessons/12949
# 행렬의 곱셈

def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(answer)):
        for j in range(len(answer[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer


# https://programmers.co.kr/learn/courses/30/lessons/12946
# 하노이의 탑

def hanoi(n, start, dest, temp, result):
    if n == 1:
        result.append([start, dest])
        return
    hanoi(n-1, start, temp, dest, result)
    result.append([start, dest])
    hanoi(n-1, temp, dest, start, result)

def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer

# 다른 풀이
def hanoi(n, start, dest, temp, result):
    if n == 1:
        return [[start, dest]]
    return hanoi(n-1, start, temp, dest, result) + [[start, dest]] + hanoi(n-1, temp, dest, start, result)

def solution(n):
    return hanoi(n, 1, 3, 2, [])


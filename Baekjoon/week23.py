# https://www.acmicpc.net/problem/1012
# 유기농 배추

from collections import deque
cases = int(input())
test_case = []
infos = [[] for i in range(cases)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(n, m):
    global queue
    global visited
    x, y = 0, 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            if 0 <= x + dx[i] < m and 0 <= y + dy[i] < n:
                if matrix[x + dx[i]][y + dy[i]] == 1 and visited[x + dx[i]][y + dy[i]] == 0:
                    queue.append((x + dx[i], y + dy[i]))
                    visited[x + dx[i]][y + dy[i]] = 1


for i in range(cases):
    infos[i] = list(map(int, input().split()))
    matrix = [[0 for j in range(infos[i][0])] for k in range(infos[i][1])]
    visited = [[0 for i in range(infos[i][0])] for j in range(infos[i][1])]
    queue = deque()
    count = 0
    for _ in range(infos[i][2]):
        b, a = map(int, input().split())
        matrix[a][b] = 1
    test_case.append(matrix)
    for j in range(infos[i][1]):
        for k in range(infos[i][0]):
            if matrix[j][k] == 1 and visited[j][k] == 0:
                queue.append((j, k))
                bfs(infos[i][0], infos[i][1])
                count += 1
    print(count)


# https://www.acmicpc.net/problem/1074
# Z


N, r, c = map(int, input().split()) # r행 c열

count = 0
x = 2**N
while x > 1:
    if x // 2 > r:
        if x // 2 > c:
            # 2 사분면
            count += 0
        else:
            # 1 사분면
            count += x*x*(1/4)
    else:
        if x // 2 > c:
            # 3 사분면
            count += x*x*(1/2)
        else:
            # 4 사분면
            count += x*x*(3/4)

    x //= 2
    r %= x
    c %= x

print(int(count))


# https://www.acmicpc.net/problem/1107
# 리모컨

N = int(input())
M = int(input())
broken = set()
if M != 0:
    broken = set(input().split())

now = 100
answer = abs(now-N) # 최악의 경우 +또는 -로만 움직임
for channel in range(1000001):
    channel_str = str(channel)
    for n in channel_str:
        if n in broken:
            break
    else:
        answer = min(answer, abs(channel-N) + len(channel_str))

print(answer)


# DFS와 BFS 
# https://www.acmicpc.net/problem/1260

from collections import deque


N, M, V = map(int, input().split())
adjacent_list = [
    [] for _ in range(N+1)
]
visited = [False for _ in range(N+1)]
dfs_result = []
bfs_result = []

for _ in range(M):
    a, b = map(int, input().split())
    adjacent_list[a].append(b)
    adjacent_list[b].append(a)

for i in range(1, N+1):
    adjacent_list[i] = sorted(adjacent_list[i])

def dfs(v):
    global visited
    
    if not visited[v]:
        visited[v] = True
        dfs_result.append(v)
        for neighbor in adjacent_list[v]:
            dfs(neighbor)

def bfs(v):
    visited = [False for _ in range(N+1)]

    queue = deque([v])
    visited[v] = True
    bfs_result.append(v)
    while queue:
        now = queue.popleft()
        for neighbor in adjacent_list[now]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                bfs_result.append(neighbor)

dfs(V)
bfs(V)

print(*dfs_result)
print(*bfs_result)
        

# https://programmers.co.kr/learn/courses/30/lessons/12945
# 피보나치 수

def solution(n):
    answer = [0, 1, 1]
    for i in range(3, n + 1) :
        answer.append(answer[i-1] + answer[i-2])
    
    
    return (answer[n]) % 1234567


# https://programmers.co.kr/learn/courses/30/lessons/12941
# 최솟값 만들기

def solution(A, B) :
    answer = 0
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)) :
        answer += A[i] * B[i]

    return answer


# https://programmers.co.kr/learn/courses/30/lessons/12939
# 최댓값과 최솟값

def solution(s):
    answer = sorted(map(int, s.split(" ")))
    answer = str(answer[0]) + " " + str(answer[-1])
    return answer


# https://programmers.co.kr/learn/courses/30/lessons/92341
# 주차 요금 계산

import math
from collections import defaultdict

def solution(fees, records):
    answer = []

    dict = {}
    total = defaultdict(int)
    # 주차한 시간
    for record in records :
        time, number, state = record.split() # 시간, 차량 번호, 상태(In or Out)
        hour, minutes = time.split(":")
        time = int(hour) * 60 + int(minutes)
        if number in dict : # 이미 입차되어 있다면
            total[number] += time - dict[number]
            del dict[number]
        else : # 입차할 경우
            dict[number] = time

    # 출차를 안 한 경우
    max_time = (23 * 60) + 59
    for num, t in dict.items():
        total[num] += max_time - t

    # 요금 계산
    basic_minutes, basic_fee, split_minutes, split_fee = fees
    for num, t in total.items() :
        cost = basic_fee
        if t > basic_minutes : # 추가 요금 발생
            cost += math.ceil((t - basic_minutes) / split_minutes) * split_fee # 올림 처리
        answer.append((num, cost))

    # 차량 번호 오름차순
    answer.sort()
    return [value[1] for value in answer]

# https://programmers.co.kr/learn/courses/30/lessons/12936
# 줄 서는 방법

import math
def solution(n, k):
    arr = [i for i in range(1, n+1)]
    answer = []
    while n > 0:
        n -= 1
        fac = math.factorial(n)
        div = k // fac
        mod = k % fac
        if mod == 0:
            div -= 1
        answer.append(arr.pop(div))
        k = mod
    return answer
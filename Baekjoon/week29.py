# # https://www.acmicpc.net/problem/5430
# # AC

# from collections import deque


# T = int(input())

# def AC():
#     p = input()
#     n = int(input())

#     nums = input()[1:-1]
#     if len(nums) > 0:
#         nums = deque(nums.split(","))

#     result = nums
#     straight = True
#     front = 0
#     back = n-1
#     for op in p:
#         if op == "R":
#             straight = not straight
#         elif op == "D":
#             if back < front:
#                 result = "error"
#                 return result
#             else:
#                 if straight:
#                     front += 1
#                 else:
#                     back -= 1
    
#     result = list(result)
#     result = result[front:back+1]
#     if straight:
#         result = '[' + ','.join(result) + ']'
#         return result
#     else:
#         result = '[' + ','.join(list(reversed(result))) + ']'
#         return result

# for _ in range(T):
#     print(AC())


# # https://www.acmicpc.net/problem/5525
# # IOIOI

# N = int(input())
# pn = "I" + "OI" * N

# M = int(input())
# S = input()

# cnt = 0
# temp = 0
# size = 2 * N + 1
# i = 1
# while i < M-2:
#     if S[i] == "O" and S[i+1] == "I":
#         temp += 1
#         if temp >= N:
#             if S[i-(2*N-1)] == "I": 
#                 cnt += 1
#                 temp -= 1
#         i += 2
#     else:
#         temp = 0
#         i += 1

# print(cnt)


# from math import gcd


# T = int(input())
# for _ in range(T):
#     M, N, x, y = map(int, input().split())

#     smaller = min(x, y)
#     temp_x = smaller
#     temp_y = smaller
#     gap = N
#     if smaller == x:
#         gap = M

#     year = smaller
#     end = M * N // gcd(M, N)

#     answer = -1

#     if temp_x == x and temp_y == y:
#         answer = year
#     else:
#         while year <= end:
#             year += gap
#             temp_x = year % M
#             temp_y = year % N

#             if temp_x == 0:
#                 temp_x = M
#             if temp_y == 0:
#                 temp_y = N

#             if temp_x != x or temp_y != y:
#                 continue
#             else:
#                 answer = year
#                 break
#     print(answer)


# from math import gcd


# T = int(input())
# for _ in range(T):
#     M, N, x, y = map(int, input().split())

#     smaller = min(x, y)
#     temp_x = smaller
#     temp_y = smaller
#     gap = N
#     if smaller == x:
#         gap = M

#     year = smaller
#     end = M * N // gcd(M, N)

#     answer = -1

#     if temp_x == x and temp_y == y:
#         answer = year
#     else:
#         while year <= end:
#             year += gap
#             temp_x = year % M
#             temp_y = year % N

#             if temp_x == 0:
#                 temp_x = M
#             if temp_y == 0:
#                 temp_y = N

#             if temp_x != x or temp_y != y:
#                 continue
#             else:
#                 answer = year
#                 break
#     print(answer)


# from collections import deque
# n, m, h = map(int, input().split())
# matrix = []
# floor = []
# dx = [0, 1, 0, -1, 0, 0]
# dy = [-1, 0, 1, 0, 0, 0]
# dz = [0, 0, 0, 0, 1, -1]
# queue = deque()
# count = 0

# for i in range(h):
#     for _ in range(m):
#         floor.append(list(map(int, input().split())))
#     matrix.append(floor)
#     floor = []

# def bfs():
#     global queue
#     global count
#     z, x, y = 0, 0, 0

#     while queue:
#         z, x, y = queue.popleft()

#         for i in range(6):
#             if 0 <= x + dx[i] < m and 0 <= y + dy[i] < n and 0 <= z + dz[i] < h:
#                 if matrix[z + dz[i]][x + dx[i]][y + dy[i]] == 0:
#                     queue.append((z + dz[i], x + dx[i], y + dy[i]))
#                     matrix[z + dz[i]][x + dx[i]][y + dy[i]] = matrix[z][x][y] + 1
#                     count += 1
#     return [matrix[z][x][y]-1, count]


# def tomato():
#     global queue
#     global count
#     all_ripe = True
#     result = 0
#     for z in range(len(matrix)):
#         for i in range(len(matrix[z])):
#             for j in range(len(matrix[z][i])):
#                 if matrix[z][i][j] == 1:
#                     queue.append((z, i, j))
#                     count += 1
#                 elif matrix[z][i][j] == 0:
#                     all_ripe = False
#                 else:
#                     count += 1
#     if all_ripe:
#         return result
#     result, count = bfs()
#     if count != n * m * h:
#         result = -1
#     return result


# print(tomato())


# https://school.programmers.co.kr/learn/courses/30/lessons/12902?language=python3#
# 3 x n 타일링

# 모르겠다!!!!!!!!!!!!!!!!!!!!!! 검색 및 다시 차근차근 생각해서 겨우 풂

# def solution(n):
#     if n % 2 == 1:
#         return 0
    
#     dp = [0 for _ in range(n//2+1)]
#     dp[0] = 1
#     dp[1] = 3

#     for i in range(2, len(dp)):
#         dp[i] = dp[i-1] * dp[1]
#         for j in range(i-1):
#             dp[i] += 2 * dp[j]
    
#     return dp[n//2] % 1000000007

# print(solution(4)) # 11
# print(solution(6)) # 41
# print(solution(8)) # 153


# # https://school.programmers.co.kr/learn/courses/30/lessons/12980
# # 점프와 순간 이동

# def solution(n):
#     if n == 1:
#         return 1
#     if n%2 == 0:
#         return solution(n//2)
#     else:
#         return solution(n-1) + 1

# print(solution(5)) # 2
# print(solution(6)) # 2
# print(solution(5000)) # 5


# # https://school.programmers.co.kr/learn/courses/30/lessons/70129
# # 이진 변환 반복하기

# def solution(s):
#     answer = [0, 0] # 이진 변환 횟수, 제거한 0의 개수
    
#     while s != "1":
#         zero = s.count('0')
#         answer[1] += zero
#         answer[0] += 1
#         s = str(bin(len(s) - zero))[2:]
        
#     return answer


# https://school.programmers.co.kr/learn/courses/30/lessons/17680
# [1차] 캐시

# LRU의 개념을 다시 공부했더니 해결. 최신화를 해줘야함

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cacheHit = 1
    cacheMiss = 5
    if cacheSize == 0:
        return len(cities) * cacheMiss

    cache = deque()
    for city in cities:
        city = city.lower()
        if city not in cache: # 캐시 미스
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city)
            answer += cacheMiss

        else: # 캐시 히트
            answer += cacheHit
            cache.remove(city)
            cache.append(city)
            
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) # 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])) # 21
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) # 60
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) # 52
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])) # 16
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) # 25 
print(solution(3, ["A","B","A"])) # 11


# https://school.programmers.co.kr/learn/courses/30/lessons/12905
# 가장 큰 정사각형 찾기

# 몰라서 검색해서 풂. dfs 이런건줄 알았는데 dp라니..
def solution(board):
    total = 0
    for b in board:
        total += sum(b)
    answer = 1 if total else 0
    
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if 0 not in (board[i-1][j-1], board[i-1][j], board[i][j-1], board[i][j]):
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                answer = max(answer, board[i][j])
    
    return answer ** 2
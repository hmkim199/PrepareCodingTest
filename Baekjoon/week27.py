# https://www.acmicpc.net/problem/1927
# 최소 힙

import sys
import heapq

heap = []
result = []

N = int(input())
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x > 0:
        heapq.heappush(heap, x)
    elif x == 0:
        res = 0
        if heap:
            res = heapq.heappop(heap)
        result.append(res)

print(*result, sep="\n")


# https://www.acmicpc.net/problem/1931
# 회의실 배정

N = int(input())
meetings = []
for _ in range(N):
    meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda x: x[0])
meetings.sort(key=lambda x: x[1])

schedule = []
schedule.append(meetings[0])
for i in range(1, N):
    if meetings[i][0] >= schedule[-1][1]:
        schedule.append(meetings[i])
    
print(len(schedule))


# https://www.acmicpc.net/problem/1992
# 쿼드트리

N = int(input())
video = []
for _ in range(N):
    video.append(list(map(int, list(input()))))

def quadtree(x, y, n):
    for i in range(n):
        for j in range(n):
            if video[x+i][y+j] != video[x][y]:
                temp = ""
                new_n = n//2
                for k in range(2):
                    for l in range(2):
                        temp += quadtree(x + k * new_n, y + l * new_n, new_n)
                temp = "(" + temp + ")"
                return temp
    return str(video[x][y])

print(quadtree(0, 0, N))


# https://www.acmicpc.net/problem/2178
# 미로 탐색

from collections import deque


N, M = map(int, input().split())

maze = []
predecessor = [[[] for _ in range(M)] for _ in range(N)]
for _ in range(N):
    maze.append(list(map(int, list(input()))))

directions = [(1, 0), (0, -1), (-1, 0), (0, 1)] # 오른쪽 아래 왼쪽 위

queue = deque([(0, 0)])
predecessor[0][0] = None

while queue:
    x, y = queue.popleft()
    for dx, dy in directions:
        if 0 <= x + dx < N and 0 <= y + dy < M:
            if not predecessor[x+dx][y+dy] and maze[x+dx][y+dy] == 1:
                predecessor[x+dx][y+dy] = [x, y]
                queue.append((x+dx, y+dy))
                if x+dx == N-1 and y+dy == M-1:
                    queue = None
                    break

temp = [N-1, M-1]
distance = 1
while temp != [0, 0]:
    distance += 1
    temp = predecessor[temp[0]][temp[1]]
print(distance)



# https://school.programmers.co.kr/learn/courses/30/lessons/17686
# [3차] 파일명 정렬

def solution(files):
    answer = []
    for file in files:
        head = ''
        num = ''
        found_num = False
        finish_num = False
        for i in range(len(file)):
            
            if not finish_num and file[i].isdigit():
                found_num = True
                num += file[i]
            elif found_num:
                finish_num = True
            elif not found_num:
                head += file[i]
            
        
        answer.append([file, head.lower(), int(num)])
    answer.sort(key=lambda x: (x[1], x[2]))
    
    new_files = []
    for ans in answer:
        new_files.append(ans[0])
    return new_files

# https://school.programmers.co.kr/learn/courses/30/lessons/17684
# [3차] 압축

# 검색해서 풂
def solution(msg):
    answer = []

    dictionary = {chr(i): i - 64 for i in range(65, 91)}
    stack = list(map(str, msg[::-1]))
    idx = 27

    while stack:
        w = stack.pop()
        if stack:
            while dictionary.get(w + stack[-1]):
                w += stack.pop()
                if len(stack) == 0: break
            answer.append(dictionary.get(w))
            if stack:
                dictionary[w + stack[-1]] = idx
            idx += 1
        else:
            answer.append(dictionary.get(w))

    return answer


# https://school.programmers.co.kr/learn/courses/30/lessons/12905
# 가장 큰 정사각형 찾기





# https://school.programmers.co.kr/learn/courses/30/lessons/17683
# [3차] 방금그곡


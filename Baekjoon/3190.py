# https://www.acmicpc.net/problem/3190
# 뱀

"""
# 핵심 아이디어

아래 방향 기준 상대적 왼쪽 방향 -> 절대적 오른쪽 방향
아래 방향 기준 상대적 오른쪽 방향 -> 절대적 왼쪽 방향

왼쪽 방향 기준 상대적 왼쪽 방향 -> 절대적 아래 방향
왼쪽 방향 기준 상대적 오른쪽 방향 -> 절대적 위 방향

위 방향 기준 상대적 왼쪽 방향 -> 절대적 왼쪽 방향
위 방향 기준 상대적 오른쪽 방향 -> 절대적 오른쪽 방향

오른쪽 방향 기준 상대적 왼쪽 방향 -> 절대적 위 방향
오른쪽 방향 기준 상대적 오른쪽 방향 -> 절대적 아래 방향

이므로 

# move에서 현재 방향 왼쪽으로 이동 경우 (현재 방향 인덱스 - 1)%4,
# 오른쪽으로 이동하는 경우 (현재 방향 인덱스 + 1)%4 하면 해당 방향!

# 뱀의 몸통은 deque로 설정해서 머리를 appendleft로 앞에 붙여주고 꼬리는 pop으로 제거하기.
"""

from collections import deque


N = int(input())
K = int(input())
move = [(1, 0), (0, -1), (-1, 0), (0, 1)] # 아 왼 위 오

dir = 3 # 현재 방향은 오른쪽
board = [[False for _ in range(N+1)] for _ in range(N+1)]
for _ in range(K):
    row, col = map(int, input().split())
    board[row][col] = True

L = int(input())
change = deque()
for _ in range(L):
    X, C = input().split()
    change.append([X, C])

time = 0
snake = deque([[1, 1]])
while True:
    if change and time == int(change[0][0]):
        x, c = change.popleft()
        if c == "D": # 오른쪽
            dir = (dir+1)%4
        else:
            dir = (dir-1)%4

    time += 1
    head = snake[0]
    x = head[0] # row
    y = head[1] # col
    dx = move[dir][0]
    dy = move[dir][1]
    if 0 < x+dx <= N and 0 < y+dy <= N:
        if [x+dx, y+dy] in snake: # 몸에 부딪힌 경우
            break
        snake.appendleft([x+dx, y+dy]) # 머리 추가
        if not board[x+dx][y+dy]: # 사과 없으면
            snake.pop() # 꼬리 지우기
        else:
            board[x+dx][y+dy] = False # 사과 없애기
    else: # 벽에 부딪힌 경우
        break

print(time)



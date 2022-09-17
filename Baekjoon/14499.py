# https://www.acmicpc.net/problem/14499
# 주사위 굴리기

"""
주사위는 지도 위에 윗 면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있으며, 놓여져 있는 곳의 좌표는 (x, y) 이다. 가장 처음에 주사위에는 모든 면에 0이 적혀져 있다.
라는 문제 설명이 오해의 여지가 많다.

-> 질문 검색에서 보니, 모든 면이 0이라고 생각하고 풀면 된다. 전개도는 그냥 힌트용으로 준 것 같다고 한다.

https://donggoolosori.github.io/2020/11/09/boj-14499/
참고했음.
"""

N, M, x, y, k = map(int, input().split())
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

# 1, 2, 3, 4 -> 동 서 북 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

move = list(map(int, input().split())) # 동 서 남 북 -> 1, 2, 4, 3

dice = [0 for _ in range(7)] # 0, 위, 북, 동, 서, 남, 아래 (숫자)

answer = []

def roll_east(dice):
    dice = [0, dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]]
    return dice

def roll_west(dice):
    dice = [0, dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]]
    return dice

def roll_north(dice):
    dice = [0, dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]]
    return dice

def roll_south(dice):
    dice = [0, dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]]
    return dice

for dir in move:
    if 0 <= x + dx[dir] < N and 0 <= y + dy[dir] < M:
        # 주사위 위치 업데이트
        x += dx[dir]
        y += dy[dir]

        # 주사위 굴리기
        if dir == 1:
            dice = roll_east(dice)
        elif dir == 2:
            dice = roll_west(dice)
        elif dir == 3:
            dice = roll_north(dice)
        else:
            dice = roll_south(dice)
        
        # 보드와 바닥면 숫자 확인, 변경
        if board[x][y] == 0:
            board[x][y] = dice[6]
        else:
            dice[6] = board[x][y]
            board[x][y] = 0
        
        answer.append(dice[1])
    
print(*answer, sep="\n")
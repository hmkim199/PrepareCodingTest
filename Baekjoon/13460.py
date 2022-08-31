# https://www.acmicpc.net/problem/13460
# 구슬 탈출 2

from collections import deque


N, M = map(int, input().split())
board = [[None for _ in range(M)] for _ in range(N)]
red = blue = hole = 0, 0

for i in range(N):
    s = input()
    for j in range(M):
        board[i][j] = s[j]
        if s[j] == "R":
            red = i, j
            board[i][j] = "."
        elif s[j] == "B":
            blue = i, j
            board[i][j] = "."
        elif s[j] == "O":
            hole = i, j

visited = set()
visited.add((red, blue))

# 가는 방향에 장애물 없는 곳까지 이동하는 함수
def go_straight(target, dx, dy, red, blue):
    global board

    new_x = target[0] + dx
    new_y = target[1] + dy
    
    while board[new_x][new_y] == "." and (new_x, new_y) not in (red, blue):  
        target = new_x, new_y
        new_x = target[0] + dx
        new_y = target[1] + dy
    
    if (new_x, new_y) == hole: # 구멍이면 구멍으로 이동
        target = new_x, new_y
        
    return target

def marble(R, B, O):
    min_move = 11
    q = deque([(R, B, 0)]) # 0은 move

    while q:
        red, blue, move = q.popleft()        
        if move > 10:
            continue

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            # 먼저 R 이동. 이동 후 R 다음 칸이 B이면 B 먼저 이동 후 다시 R 이동.
            R = go_straight(red, dx, dy, red, blue)
            B = go_straight(blue, dx, dy, R, blue)
            
            if B == O:
                continue
            
            if R == O:
                return move + 1
            
            if (R[0]+dx, R[1]+dy) == blue:
                R = go_straight(R, dx, dy, R, B)

            if (red != R or blue != B) and (R, B) not in visited:
                visited.add((R, B))
                q.append((R, B, move+1))
        
    return min_move

count = marble(red, blue, hole)
if count > 10:
    print(-1)
else:
    print(count)
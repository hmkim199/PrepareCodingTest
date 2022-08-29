# https://www.acmicpc.net/problem/13460
# 구슬 탈출 2

# 86퍼에서 틀렸습니다
from collections import deque


N, M = map(int, input().split())
board = [[None for _ in range(M)] for _ in range(N)]
red = 0, 0
blue = 0, 0
hole = 0, 0

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

def go_straight(target, dx, dy, red, blue, visited = None):
    global board

    new_x = target[0] + dx
    new_y = target[1] + dy
    
    while board[new_x][new_y] == "." and (new_x, new_y) not in (red, blue):  
        target = new_x, new_y
        new_x = target[0] + dx
        new_y = target[1] + dy
    
    if (new_x, new_y) == hole:
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
            R = go_straight(red, dx, dy, red, blue, visited)
            if (R[0]+dx, R[1]+dy) == blue:
                B = go_straight(blue, dx, dy, R, blue)
                if (B[0]+dx, B[1]+dy) == hole:
                    continue
                if R == hole:
                    return move + 1
                R = go_straight(R, dx, dy, R, B, visited)
            
            else:
                B = go_straight(blue, dx, dy, R, blue)
                if R == hole:
                    if R != B:
                        # min_move = min(min_move, move+1)
                        return move + 1
                    continue
                elif B == hole:
                    continue

            if red != R or blue != B:
                if (R, B) not in visited:
                    visited.add((R, B))
                    q.append((R, B, move+1))
        
    return min_move

count = marble(red, blue, hole)
if count > 10:
    print(-1)
else:
    print(count)
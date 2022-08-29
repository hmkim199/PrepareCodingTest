# https://www.acmicpc.net/problem/13460
# 구슬 탈출 2


# 음.. 일단 실제 board를 바꾸면 안될것같음. 뭔가 접근법은 비슷한거같으면서..... 조금 더 생각해보기로!!!!!!!!

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

visited = [[False for _ in range(M)] for _ in range(N)]
visited[red[0]][red[1]] = True 

def go_straight(target, dx, dy, color):
    global board
    global visited
    # global red
    # global blue
    # global N
    # global M

    # is_moved = False
    new_x = target[0] + dx
    new_y = target[1] + dy
    
    while board[new_x][new_y] == "." and (new_x, new_y) not in (red, blue): # 0 <= new_x < N and 0 <= new_y < M and 
        # board[new_x][new_y] = color
        # if color == "B":
        #     blue = new_x, new_y
        # else:
        #     red = new_x, new_y
        visited[new_x][new_y] = True        
        # board[target[0]][target[1]] = "."
        # is_moved = True
        target = new_x, new_y
        new_x = target[0] + dx
        new_y = target[1] + dy
        
    # return is_moved, new_x, new_y
    return target

def marble(R, B, O):
    min_move = -1
    q = deque([(R, B, 0)]) # 0은 move

    while q:
        red, blue, move = q.popleft()        
        if move > 10:
            continue

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            # is_moved = False
            # temp_moved, R_x, R_y = go_straight(red, dx, dy, "R")
            R = go_straight(red, dx, dy, "R")
            # if temp_moved:
            #     is_moved = True
            
            # if board[R_x][R_y] == "B":
            if (R[0]+dx, R[1]+dy) == blue:
                # temp_moved, B_x, B_y = go_straight(blue, dx, dy, "B")
                B = go_straight(blue, dx, dy, "B")
                # if board[B_x][B_y] == "O":
                if (B[0]+dx, B[1]+dy) == hole:
                    continue
                # R = R_x - dx, R_y - dy
                # temp_moved, R_x, R_y = go_straight(red, dx, dy, "R")
                R = go_straight(R, dx, dy, "R")

                # if temp_moved:
                #     is_moved = True
            
            else:
                # temp_moved, B_x, B_y = go_straight(blue, dx, dy, "B")
                B = go_straight(blue, dx, dy, "B")


            # if is_moved:
            if red != R:
                new_move = move + 1
                # new_R = R_x - dx, R_y - dy
                # new_B = B_x - dx, B_y - dy
                q.append((R, B, new_move))

            if board[R[0]+dx][R[1]+dy] == "O":
                min_move = min(min_move, new_move)
        
    return move

print(marble(red, blue, hole))
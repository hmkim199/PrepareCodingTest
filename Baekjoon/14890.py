# https://www.acmicpc.net/problem/14890
# 경사로

N, L = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

count = 0
for i in range(N):
    # row = []
    # # row 검사.
    # for j in range(N):
    #     if row:
    #         if board[i][j-1] == board[i][j]:
    #             row[1] += 1
    #             continue
    #         elif abs(board[i][j-1] - board[i][j]) != 1:
    #             break
    #         elif board[i][j-1] < board[i][j]:
    #             if row[1] < L:
    #                 break
    #     row = [board[i][j], 1]
    # else:
    #     if row[1] >= L:
    #         count += 1
    
    col = []
    check = False
    for j in range(N):
        if col:
            if board[j-1][i] == board[j][i]:
                col[1] += 1
                continue
            elif abs(board[j-1][i] - board[j][i]) != 1:
                break
            elif board[j-1][i] < board[j][i]:
                if col[1] < L or check:
                    break
            else:
                if check:
                    if col[1] < L:
                        break
                check = True
        col = [board[j][i], 1]
    else:
        if col[1] >= L:
            count += 1

print(count)
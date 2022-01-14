N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(input())

minimum = N * M
for i in range(N-7):
    for j in range(M-7):
        first_black = 0
        first_white = 0
        for k in range(8):
            for w in range(8):
                if (k%2 == 0 and w%2 == 0) or (k%2 == 1 and w%2 == 1):
                    if board[k+i][w+j] == "B":
                        first_white += 1
                    else:
                        first_black += 1
                else:
                    if board[k+i][w+j] == "B":
                        first_black += 1
                    else:
                        first_white += 1

        # print(minimum, first_black, first_white)                
        minimum = min(minimum, first_black, first_white)

print(minimum)

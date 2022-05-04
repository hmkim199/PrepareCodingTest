# https://www.acmicpc.net/problem/1018
# 체스판 다시 칠하기

# N, M = map(int, input().split())

# board = []
# for i in range(N):
#     board.append(input())

# minimum = N * M
# for i in range(N-7):
#     for j in range(M-7):
#         first_black = 0
#         first_white = 0
#         for k in range(8):
#             for w in range(8):
#                 if (k%2 == 0 and w%2 == 0) or (k%2 == 1 and w%2 == 1):
#                     if board[k+i][w+j] == "B":
#                         first_white += 1
#                     else:
#                         first_black += 1
#                 else:
#                     if board[k+i][w+j] == "B":
#                         first_black += 1
#                     else:
#                         first_white += 1

#         # print(minimum, first_black, first_white)                
#         minimum = min(minimum, first_black, first_white)

# print(minimum)


N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(input())


min_count = 1e9
for k in range(N-7):
    for l in range(M-7):
        repaint_w = 0
        repaint_b = 0
        for i in range(8):
            for j in range(8):
                # 제일 왼쪽 위칸이 흰색 -> (짝수, 짝수), (홀수, 홀수)가 흰색
                # 제일 왼쪽 위칸이 검정색 -> (짝수, 짝수), (홀수, 홀수)가 검정색
                if (i-j) % 2 == 0:
                    if board[k+i][l+j] == "B":
                        repaint_w += 1
                    else:
                        repaint_b += 1
                else:
                    if board[k+i][l+j] == "W":
                        repaint_w += 1
                    else:
                        repaint_b += 1
        min_count = min(min_count, repaint_w, repaint_b)

print(min_count)
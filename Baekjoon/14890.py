# https://www.acmicpc.net/problem/14890
# 경사로

N, L = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def slope(board):
    info = [board[0], 1] # 숫자, count
    decrease = False # 감소된 상태인지 flag
    for j in range(1, N):
        if board[j-1] == board[j]: # 이전 값과 같으면 count + 1
            info[1] += 1
            continue
        elif abs(board[j-1] - board[j]) != 1: # 1보다 차이 크면 다음 줄 확인
            break
        elif board[j-1] < board[j]: # 증가한 경우
            if info[1] < L or (decrease and info[1] < L*2): # count가 L보다 작으면 경사로 설치 못함, 이전에 감소된 경우(decrease) count가 L*2보다 작으면 경사로 설치 못함 (3 2 2 3 같은 경우 L=2일 때 설치 못함)
                break
            decrease = False
        else: # 감소한 경우
            if decrease and info[1] < L: # 이전에도 감소된 경우라면 count가 L보다 작으면 경사로 설치 불가. (3 2 1 의 경우 L=2일때 불가)
                break
            decrease = True
        info = [board[j], 1] # 이전 숫자와 count 업데이트
    else:
        if not decrease or info[1] >= L: # 증가된 경우거나(경사로 설치 못하는 경우 for문에서 다 걸러졌으므로) count가 L이상이면(감소된 경우라면. 3 2 2 경우 L=2일때 가능) 1 리턴
            return 1
    return 0

count = 0
for i in range(N):
    count += slope(board[i]) # row 검사
    count += slope([board[j][i] for j in range(N)]) # col 검사

print(count)
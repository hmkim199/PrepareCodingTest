# https://www.acmicpc.net/problem/5525
# IOIOI


# 틀린 50점 풀이 -> n, M 커지면 시간 초과!!!!
N = int(input())
pn = "I" + "OI" * N

M = int(input())
S = input()

cnt = 0
size = len(pn)
for i in range(len(S) - size + 1):
    if S[i:i+size] == pn:
        cnt += 1

print(cnt)


# 시간 초과 때문에 50점에서 한참 머물다가 방식 수정.

N = int(input())
M = int(input())
S = input()

cnt = 0
temp = 0
size = 2 * N + 1
i = 1
while i < M-2:
    if S[i] == "O" and S[i+1] == "I":
        temp += 1
        if temp >= N:
            if S[i-(2*N-1)] == "I": 
                cnt += 1
                temp -= 1
        i += 2
    else:
        temp = 0
        i += 1

print(cnt)
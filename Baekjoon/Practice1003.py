# https://www.acmicpc.net/problem/1003
# 피보나치 함수

#              0 1 2 3 4 5 6
# 0 출력 횟수 - 1 0 1 1 2 
# 1 출력 횟수 - 0 1 1 2

fibo = []

for i in range(41):
    if i == 0:
        fibo.append((1, 0))
    elif i == 1:
        fibo.append((0, 1))
    else:
        fibo.append((fibo[i-1][0]+fibo[i-2][0], fibo[i-1][1]+fibo[i-2][1]))


T = int(input())
for i in range(T):
    N = int(input())
    print(*fibo[N])
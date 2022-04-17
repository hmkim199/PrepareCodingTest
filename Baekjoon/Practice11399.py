# https://www.acmicpc.net/problem/11399
# ATM

N = int(input())
waiting = sorted(list(map(int, input().split())))

time = 0
for i in range(N):
    time += sum(waiting[:i+1])
print(time)
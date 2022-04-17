# https://www.acmicpc.net/problem/11047
# 동전 0

N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

change = K
cnt = 0
for i in range(N-1, -1, -1):
    if change >= coins[i]: # 같은 경우를 꼭 넣어주자...
        cnt += change // coins[i]
        change = change % coins[i]
print(cnt)
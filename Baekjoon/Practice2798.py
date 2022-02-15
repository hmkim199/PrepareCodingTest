# https://www.acmicpc.net/problem/2798
# 블랙잭

N, M = map(int, input().split())
cards = list(map(int, input().split()))

total = 0
length = len(cards)
for i in range(length-2):
    for j in range(i+1, length-1):
        for k in range(j+1, length):
            temp = cards[i] + cards[j] + cards[k]
            if total < temp <= M:
                total = temp

print(total)
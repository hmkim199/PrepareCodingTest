# https://www.acmicpc.net/problem/10816
# 숫자 카드 2

import sys

N = int(input())
my_cards = sys.stdin.readline().strip().split()
cards_count = {}
for card in my_cards:
    if card in cards_count:
        cards_count[card] += 1
    else:
        cards_count[card] = 1

M = int(input())
given_cards = sys.stdin.readline().strip().split()

counts = []
for card in given_cards:
    if card in cards_count:
        counts.append(cards_count[card])
    else:
        counts.append(0)

print(*counts, sep=" ")

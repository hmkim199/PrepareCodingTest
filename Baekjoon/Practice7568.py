# https://www.acmicpc.net/problem/7568
# 덩치

N = int(input())
people = []
for _ in range(N):
    w, h = map(int, input().split())
    people.append((w, h))

rank = [1] * len(people)
for i in range(len(people)):
    for person in people[:i]+people[i+1:]:
        if people[i][0] < person[0] and people[i][1] < person[1]:
            rank[i] += 1

print(*rank, sep=" ")
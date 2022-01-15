# https://www.acmicpc.net/problem/1181
# 단어 정렬

N = int(input())

words = []
for i in range(N):
    words.append(input().strip())

words = list(set(words))
words.sort()
words.sort(key=len)
print(*words, sep="\n")
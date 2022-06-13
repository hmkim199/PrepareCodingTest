# https://www.acmicpc.net/problem/1780
# 종이의 개수

paper = []
N = int(input())
for _ in range(N):
    paper.append(list(map(int, input().split())))

cnt = {-1: 0, 0: 0, 1: 0}

def count_paper(x, y, n):
    global cnt
    for i in range(n):
        for j in range(n):
            if paper[x+i][y+j] != paper[x][y]:
                for k in range(3):
                    for l in range(3):
                        new_n = n//3 
                        count_paper(x + new_n * k, y + new_n * l, new_n)
                return
    cnt[paper[x][y]] += 1

count_paper(0, 0, N)
print(cnt[-1])
print(cnt[0])
print(cnt[1])
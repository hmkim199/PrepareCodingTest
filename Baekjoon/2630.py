# https://www.acmicpc.net/problem/2630
# 색종이 만들기

N = int(input())
paper = []

for _ in range(N):
    paper.append(list(map(int, input().split())))

blue = 0
white = 0

def count_paper(x, y, n):
    global blue
    global white
    
    for i in range(n):
        for j in range(n):
            if paper[x+i][y+j] != paper[x][y]:
                for k in range(2):
                    for l in range(2):
                        new_n = n//2
                        count_paper(x+k*new_n, y+l*new_n, new_n)
                return
    
    if paper[x][y] == 0:
        white += 1
    else:
        blue += 1

count_paper(0, 0, N)
print(white)
print(blue)
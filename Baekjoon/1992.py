# https://www.acmicpc.net/problem/1992
# 쿼드트리

N = int(input())
video = []
for _ in range(N):
    video.append(list(map(int, list(input()))))

def quadtree(x, y, n):
    for i in range(n):
        for j in range(n):
            if video[x+i][y+j] != video[x][y]:
                temp = ""
                new_n = n//2
                for k in range(2):
                    for l in range(2):
                        temp += quadtree(x + k * new_n, y + l * new_n, new_n)
                temp = "(" + temp + ")"
                return temp
    return str(video[x][y])

print(quadtree(0, 0, N))
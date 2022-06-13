# https://www.acmicpc.net/problem/1780
# 종이의 개수

paper = []
N = int(input())
for _ in range(N):
    paper.append(list(map(int, input().split())))

cnt = {-1: 0, 0: 0, 1: 0}
# found = [[False for _ in range(N)] for _ in range(N)]

# def is_all_same(x, y, n):
#     global cnt

#     for i in range(n):
#         for j in range(n):
#             if paper[x+i][y+j] != paper[x][y]:
#                 return False
#     cnt[paper[x][y]] += 1
#     return True


# def count_paper(N):
#     if N == 1:
#         return True

#     n = N//3
#     for i in range(0, N, n):
#         for j in range(0, N, n):
#             if not is_all_same(i, j, n):
#                 count_paper(n)

# if not is_all_same(0, 0, N):
#     count_paper(N)


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
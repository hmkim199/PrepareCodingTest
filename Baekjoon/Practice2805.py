# https://www.acmicpc.net/problem/2805
# 나무 자르기 

N, M = map(int, input().split())
heights = list(map(int, input().split()))

start = 0
end = max(heights)
max_h = 0

def middle(start, end):
    return (start+end) // 2

while start <= end:
    max_h = middle(start, end)
    remain = 0
    for h in heights:
        if h > max_h:
            remain += h-max_h
    if remain < M:
        end = max_h - 1
    elif remain > M:
        start = max_h + 1
    else:
        break

print(middle(start, end))
# https://www.acmicpc.net/problem/1654
# 랜선 자르기

K, N = map(int, input().split())
lines = []

for _ in range(K):
    lines.append(int(input()))

start = 1
end = max(lines)
while start <= end:
    count = 0
    middle = (start+end)//2
    for line in lines:
        count += line // middle
    if count >= N:
        start = middle + 1
    else:
        end = middle - 1
    
print((start+end)//2)
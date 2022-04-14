# https://www.acmicpc.net/problem/17626
# Four Squares


n = int(input())
cnt = 0
while n > 0:
    temp = int(n**0.5)
    print(temp)
    n -= temp**2
    cnt += 1
print(cnt)
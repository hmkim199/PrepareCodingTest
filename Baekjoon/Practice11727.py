# https://www.acmicpc.net/problem/11727
# 2×n 타일링 2

# n=1 -> 1, n=2 -> 3, n=3 -> 5, n=4 -> 11 ... => f(n) = f(n-2)*2 + f(n-1)
n = int(input())
prev = 1
curr = 3
num = 10007
if n == 1:
    print(prev % num)
elif n == 2:
    print(curr % num)
else:
    for i in range(3, n+1):
        temp = prev
        prev = curr
        curr += temp*2
    print(curr % num)
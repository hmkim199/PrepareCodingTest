# https://www.acmicpc.net/problem/11726
# 2×n 타일링


# 피보나치! n=1 -> 1, n=2 -> 2, n=3 -> 3, n=4 -> 5

n = int(input())
prev = 1
curr = 2
num = 10007
if n == 1:
    print(prev % num)
elif n == 2:
    print(curr % num)
else:
    for i in range(3, n+1):
        temp = prev
        prev = curr
        curr += temp
    print(curr % num)

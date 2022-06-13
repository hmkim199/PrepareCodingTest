# https://www.acmicpc.net/problem/1676
# 팩토리얼 0의 개수

memo = {0: 1, 1: 1}
def factorial(i):
    if i in memo:
        return memo[i]
    else:
        memo[i] = i * factorial(i-1)
        return memo[i]

def find_zero(i):
    reversed_i = str(i)[::-1]
    idx = 0
    for num in reversed_i:
        if num != "0":
            break
        idx += 1
    return idx

num = int(input())
fact = factorial(num)
print(find_zero(fact))

# https://www.acmicpc.net/problem/2609
# 최대공약수와 최소공배수

a, b = map(int, input().split())
a, b = max(a, b), min(a, b)

def gcd(a, b):
    while True:
        r = a % b
        if r == 0:
            break
        a = b
        b = r
    return b

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))



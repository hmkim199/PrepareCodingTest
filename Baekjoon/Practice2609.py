# https://www.acmicpc.net/problem/2609
# 최대공약수와 최소공배수

# 참고 링크 : https://velog.io/@junyp1/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95 유클리드 호제법

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



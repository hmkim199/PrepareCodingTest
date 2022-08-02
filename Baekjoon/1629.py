# https://www.acmicpc.net/problem/1629
# 곱셈

# 나머지 분배법칙에 따라...
# 참고 자료: https://sexycoder.tistory.com/66
A, B, C = map(int, input().split())

def power(A, B, C):
    if B == 0:
        return 1%C
    half = power(A, B//2, C)
    if B%2 == 0:
        return (half * half) % C
    else:
        return (half * half * A) % C

print(power(A, B, C))
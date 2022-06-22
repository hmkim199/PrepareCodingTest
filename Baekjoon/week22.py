# https://programmers.co.kr/learn/courses/30/lessons/12953#
# N개의 최소공배수

# 처음엔 for문 돌면서 gcd 값으로 계속 gcd 구했는데 틀림! lcm으로 gcd 갱신해야함.

def get_gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def solution(arr):
    lcm = arr[0]
    for i in range(1, len(arr)):
        temp = lcm
        gcd = get_gcd(lcm, arr[i])
        lcm = temp * arr[i] // gcd
    return lcm


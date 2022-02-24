# https://www.acmicpc.net/problem/2869
# 달팽이는 올라가고 싶다

"""
며칠이 걸리는지를 x로 두면
ax + b(x-1) >= v
"""


import math

A, B, V = map(int, input().split())

day = math.ceil((V-B)/(A-B))
print(day)
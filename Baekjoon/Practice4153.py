# https://www.acmicpc.net/problem/4153
# 직각삼각형

isPythagoras = []

while True:
    triangle = sorted(list(map(int, input().split())))
    if triangle[0] == 0 and triangle[1] == 0 and triangle[2] == 0:
        break
    if triangle[0] ** 2 + triangle[1] ** 2 == triangle[2] ** 2:
        isPythagoras.append("right")
    else:
        isPythagoras.append("wrong")

print("\n".join(isPythagoras))
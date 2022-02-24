# https://www.acmicpc.net/problem/4153
# 직각삼각형

# 예전 풀이

# isPythagoras = []

# while True:
#     triangle = sorted(list(map(int, input().split())))
#     if triangle[0] == 0 and triangle[1] == 0 and triangle[2] == 0:
#         break
#     if triangle[0] ** 2 + triangle[1] ** 2 == triangle[2] ** 2:
#         isPythagoras.append("right")
#     else:
#         isPythagoras.append("wrong")

# print("\n".join(isPythagoras))


# 새 풀이
res=[]
while True:
    t = sorted(list(map(int, input().split())))
    if sum(t) == 0:
        break
    elif t[0]**2 + t[1]**2 == t[2]**2:
        res.append("right")
    else:
        res.append("wrong")

print(*res, sep="\n")

















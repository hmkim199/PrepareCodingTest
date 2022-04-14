# https://www.acmicpc.net/problem/10950
# A+B - 3


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(A+B)


# https://www.acmicpc.net/problem/10951
# A+B - 4

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break


# https://www.acmicpc.net/problem/10952
# A+B - 5

while True:
    A, B = map(int, input().split())
    if A+B == 0:
        break
    print(A+B)

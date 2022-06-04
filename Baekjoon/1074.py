# https://www.acmicpc.net/problem/1074
# Z


N, r, c = map(int, input().split()) # r행 c열

count = 0
x = 2**N
while x > 1:
    if x // 2 > r:
        if x // 2 > c:
            # 2 사분면
            count += 0
        else:
            # 1 사분면
            count += x*x*(1/4)
    else:
        if x // 2 > c:
            # 3 사분면
            count += x*x*(1/2)
        else:
            # 4 사분면
            count += x*x*(3/4)

    x //= 2
    r %= x
    c %= x

print(int(count))
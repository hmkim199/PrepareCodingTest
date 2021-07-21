# https://programmers.co.kr/learn/courses/30/lessons/12969
# 직사각형 별찍기

a, b = map(int, input().strip().split(' '))
#print(a + b)

for _ in range(b):
    for __ in range(a):
        print("*", end="")
    print()
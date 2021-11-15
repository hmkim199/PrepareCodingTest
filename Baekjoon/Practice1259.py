# https://www.acmicpc.net/problem/1259
# 팰린드롬수

import sys
while True:
    num = sys.stdin.readline().rstrip()
    if int(num) == 0:
        break
    isPalindrom = True
    for i in range(len(num)//2+1):
        if num[i] != num[-(i+1)]:
            isPalindrom = False
    if isPalindrom:
        print("yes")
    else:
        print("no")
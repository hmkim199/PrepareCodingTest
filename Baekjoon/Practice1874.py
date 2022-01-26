# https://www.acmicpc.net/problem/1874
# 스택 수열

n = int(input())
seq = []
stack = []
operation = []
answer = []

for _ in range(n):
    seq.append(int(input()))

seq = seq[::-1]

for i in range(1, n+1):
    if i == seq[-1]:
        operation.append("+")
        seq.pop()
        operation.append("-")
        while stack and seq and stack[-1] == seq[-1]:
            stack.pop()
            seq.pop()
            operation.append("-")
    else:
        stack.append(i)
        operation.append("+")

if seq == stack:
    print(*operation, sep="\n")
else:
    print("NO")
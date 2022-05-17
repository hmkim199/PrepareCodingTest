# https://www.acmicpc.net/problem/1874
# 스택 수열

# 시간초과
# from collections import deque


# n = int(input())
# seq = deque()
# for _ in range(n):
#     seq.append(int(input()))

# operation = []
# num = 1
# stack = deque()
# while seq:
#     if num <= seq[0]:
#         stack.append(num)
#         operation.append('+')
#         num += 1
#     if stack:
#         if stack[-1] == seq[0]:
#             stack.pop()
#             operation.append('-')
#             seq.popleft()
#         elif num > n:
#             break
        

# if stack:
#     print("NO")

# else:
#     print(*operation, sep="\n")
    
    
from collections import deque


n = int(input())
seq = deque()
for _ in range(n):
    seq.append(int(input()))

stack = deque()
operation = []

for i in range(1, n+1):
    if i == seq[0]:
        operation.append('+')
        operation.append('-')
        seq.popleft()
        while stack and stack[-1] == seq[0]:
            operation.append('-')
            seq.popleft()
            stack.pop()
    else:
        operation.append('+')
        stack.append(i)

if stack:
    print("NO")

else:
    print(*operation, sep="\n")
# https://www.acmicpc.net/problem/9012
# 괄호

T = int(input())
result = []
for _ in range(T):
    string = input()
    paren_stack = []
    right = True
    for c in string:
        if c == "(":
            paren_stack.append(c)
        else:
            try:
                paren_stack.pop()
            except:
                right = False

    if len(paren_stack) == 0 and right:
        result.append("YES")
    else:
        result.append("NO")

print(*result, sep="\n")
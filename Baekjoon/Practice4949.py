# https://www.acmicpc.net/problem/4949
# 균형잡힌 세상

paren = {"(":")", "[":"]"}
res = []

while True:
    sentence = input()
    if sentence == ".":
        break

    paren_stack = []
    right = True
    for c in sentence:
        if c in ("(", "["):
            paren_stack.append(c)
        elif c in(")", "]"):
            try:
                temp = paren_stack.pop()
                if paren[temp] != c:
                    right = False
                    break
            except:
                right = False
                break
    
    if len(paren_stack) == 0 and right:
        res.append("yes")
    else:
        res.append("no")

print(*res, sep="\n")
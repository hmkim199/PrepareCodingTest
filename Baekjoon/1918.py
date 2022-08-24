# https://www.acmicpc.net/problem/1918
# 후위 표기식

# 자료구조 자료 보고 풂. 강의 다시 듣고 원리 정리해두기!

from collections import deque


exp = input()

def convert_to_postfix(infix_exp):
    isp = {"(": 0, ")": 3, "+": 1, "-": 1, "*": 2, "/": 2}
    icp = {"(": 4, ")": 3, "+": 1, "-": 1, "*": 2, "/": 2}

    stack = deque()
    postfix = ""
    for c in infix_exp:
        # 연산자
        if c in ("+", "-", "*", "/", "("):
            while stack and isp[stack[-1]] >= icp[c]:
                    postfix += stack.pop()
            else:
                stack.append(c)

        elif c == ")":
            while stack[-1] != "(":
                postfix += stack.pop()
            if stack[-1] == "(":
                stack.pop()
        
        # 피연산자
        else:
            postfix += c

    while stack:
        postfix += stack.pop()

    return postfix

print(convert_to_postfix(exp))

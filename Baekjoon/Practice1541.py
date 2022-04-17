# https://www.acmicpc.net/problem/1541
# 잃어버린 괄호

# 규칙
# + + => 그대로
# + - => 그대로
# - + => +만 묶기
# - - => 그대로
# - + - => +만 묶기

equation = input().split("-")
result = 0
for i in range(len(equation)):
    temp = sum(map(int, equation[i].split("+")))
    if i == 0:
        result += temp
    else:
        result -= temp

print(result)
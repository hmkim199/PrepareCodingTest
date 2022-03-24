# https://www.acmicpc.net/problem/3052
# 나머지 

nums = []

for _ in range(10):
    num = int(input())
    nums.append(num%42)

print(len(set(nums)))


# https://www.acmicpc.net/problem/8958
# OX퀴즈

T = int(input())

for _ in range(T):
    testcase = input()
    answer = [0 for i in range(len(testcase))]
    for i in range(len(testcase)):
        if testcase[i] == "O":
            answer[i] += 1
            if i != 0:
                answer[i] += answer[i-1]
    print(sum(answer))


# https://www.acmicpc.net/problem/9498
# 시험 성적 

num = int(input())
if 90 <= num <= 100:
    print("A")
elif 80 <= num < 90:
    print("B")
elif 70 <= num < 80:
    print("C")
elif 60 <= num < 70:
    print("D")
else:
    print("F")